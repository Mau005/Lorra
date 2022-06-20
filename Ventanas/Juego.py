from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.graphics import Rectangle
from Entidad.Persona import Persona
from Sprites.ManejadorSprites import ManejadorSprites
from kivy.core.window import Window
from Controles.Teclado import Teclado
from core.Constantes import CANTIDAD_ESPACIOS_X ,CANTIDAD_ESPACIOS_Y

class Juego(MDScreen):
    def __init__(self, window_size, **kargs):
        super().__init__(size = window_size, **kargs)
        self.tamanio_cuadro = [window_size[0] / CANTIDAD_ESPACIOS_X ,window_size[1] / CANTIDAD_ESPACIOS_Y]
        self.pos_defecto = [self.tamanio_cuadro[0] * int(CANTIDAD_ESPACIOS_X / 2) - 77, self.tamanio_cuadro[1] * int(CANTIDAD_ESPACIOS_Y / 2)]
        print(self.tamanio_cuadro)
        self.teclado = Teclado()
        self.name = "Juego"
        self._teclado = Window.request_keyboard(self._cerrar_teclado, self, 'text')
        self._teclado.bind(on_key_down=self._precionar_tecla)
        self._teclado.bind(on_key_up = self._soltar_tecla)
        self.maya = MDFloatLayout(size = self.size, size_hint = self.size_hint)
        self.add_widget(self.maya)
        self.manejadorSprites = ManejadorSprites()
        self.jugador = Persona(self.manejadorSprites, 'Mau', 'prueba123', 1, 1, 1, 100, 100, 20, 20, 0, 1, '100:100:1', 1, self.pos_defecto, self.tamanio_cuadro)

        with self.maya.canvas.before:
            self.bg = Rectangle(size = [32,32])



    def _cerrar_teclado(self, *args):
        print("Se ha cerrado el teclado")
        self._teclado.unbind(on_key_down=self._precionar_tecla)
        self._teclado.unbind(on_key_up=self._soltar_tecla)
        self._teclado = None

    def _soltar_tecla(self, *args):
        contenido = args[1][0]
        if contenido == 119 or contenido == 115 or contenido == 97 or contenido == 100:
            self.jugador.enMovimiento = False

        self.teclado.soltar_tecla(contenido)


    def _precionar_tecla(self, *args):
        # Objetivo de 2 capturas de teclas
        # [0] posicion es espacio en memoria
        # [1] ID del teclado y letra del teclado
        # [2] la letra del teclado
        # [3] Tecla especial+ tecla
        self.teclado.precionar_tecla(args[1][0])

    def movimiento_jugador(self, dt):
        velocidad = 85 * dt[0][0]

        if self.teclado.get_tecla(119):
            self.jugador.pos[1] += velocidad
            self.jugador.direccion = "norte"
            self.jugador.enMovimiento = True
        elif self.teclado.get_tecla(115):
            self.jugador.pos[1] -= velocidad
            self.jugador.direccion = "sur"
            self.jugador.enMovimiento = True
        elif self.teclado.get_tecla(97):
            self.jugador.pos[0] -= velocidad
            self.jugador.direccion = "izquierda"
            self.jugador.enMovimiento = True
        elif self.teclado.get_tecla(100):
            self.jugador.pos[0] += velocidad
            self.jugador.direccion = "derecha"
            self.jugador.enMovimiento = True


    def actualizar(self, *dt):
        self.movimiento_jugador(dt)
        self.jugador.actualizar(dt)

    def dibujar(self, window_size, *dt):
        self.size = window_size
        self.maya.canvas.clear()
        self.jugador.dibujar(self.maya.canvas, dt)
