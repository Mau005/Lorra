from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from Entidad.Persona import Persona
from Mapa.Mapa import Mapa
from Sprites.ManejadorSprites import ManejadorSprites
from kivy.core.window import Window
from Controles.Teclado import Teclado
from core.Constantes import CANTIDAD_ESPACIOS_X, CANTIDAD_ESPACIOS_Y
from core.ControladorObjetos import ControladorObjetos
from Objetos.Suelos import Suelos
from core.Render import Render


class Juego(MDScreen):
    def __init__(self, **kargs):
        super().__init__(size=Window.size, **kargs)
        self.__configuracion_teclado()
        self.__actualizar_defecto()
        self.__configuracion_ventana()
        self.__contenido_canvas()

    def __configuracion_teclado(self):
        self._teclado = Window.request_keyboard(self._cerrar_teclado, self, 'text')
        self._teclado.bind(on_key_down=self._precionar_tecla)
        self._teclado.bind(on_key_up=self._soltar_tecla)
        self.teclado = Teclado()

    def __actualizar_defecto(self):
        self.tamanio_cuadro = [Window.size[0] / CANTIDAD_ESPACIOS_X, Window.size[1] / CANTIDAD_ESPACIOS_Y]
        self.pos_defecto = [self.tamanio_cuadro[0] * int(CANTIDAD_ESPACIOS_X / 2) - int(self.tamanio_cuadro[0] / 2),
                            self.tamanio_cuadro[1] * int(CANTIDAD_ESPACIOS_Y / 2)]

    def __configuracion_ventana(self):
        self.name = "Juego"
        self.maya = MDFloatLayout(size=self.size, size_hint=self.size_hint)
        self.add_widget(self.maya)


    def __contenido_canvas(self):
        self.manejadorSprites = ManejadorSprites()
        self.controladorObjetos = ControladorObjetos(self.manejadorSprites)
        self.jugador = Persona(self.manejadorSprites, 'Mau', 1, 10 ,11, 1, self.pos_defecto, self.tamanio_cuadro)
        self.render = Render(self.jugador, self.teclado, self.tamanio_cuadro)
        self.mapa = Mapa(100, 100, 4)

        mapa = self.mapa.get_mapa()

        for y in range(len(mapa)):
            for x in range(len(mapa[y])):
                for z in range(len(mapa[y][x])):
                    contenido = mapa[y][x][z]
                    pos = [x * self.tamanio_cuadro[0], y * self.tamanio_cuadro[1]]
                    if contenido >= 1:
                        self.render.registrar(self.controladorObjetos.get_objeto(contenido,pos,self.tamanio_cuadro))


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

    def actualizar(self, *dt):
        self.__actualizar_defecto()
        self.jugador.actualizar(dt)
        self.jugador.pos = self.pos_defecto
        self.render.actualizar(self.tamanio_cuadro, dt)

    def dibujar(self, *dt):
        self.size = Window.size
        self.maya.canvas.clear()
        self.render.dibujar(self.maya.canvas, dt)
        self.jugador.dibujar(self.maya.canvas, self.tamanio_cuadro, dt)
