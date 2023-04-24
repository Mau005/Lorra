from kivy.lang import Builder
from kivy.properties import ObjectProperty
from Entidad.Persona import Persona
from Sprites.ManejadorSprites import ManejadorSprites
from kivy.core.window import Window
from Controles.Teclado import Teclado
from Ventanas.AbstractScreen import AbstractScreen
from core.Constantes import CANTIDAD_ESPACIOS_X, CANTIDAD_ESPACIOS_Y
from core.ControladorObjetos import ControladorObjetos
from Objetos.Suelos import Suelos
from core.Render import Render

Builder.load_file("Ventanas/juego.kv")


class Juego(AbstractScreen):
    maya = ObjectProperty()

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
        self.tamanio_cuadro = [Window.size[0] / CANTIDAD_ESPACIOS_X,
                               Window.size[1] / CANTIDAD_ESPACIOS_Y]

    def __configuracion_ventana(self):
        self.manejadorSprites = ManejadorSprites()
        self.controladorObjetos = ControladorObjetos()
        self.jugador = Persona(self.manejadorSprites, 'Mau', 1, [0, 0], self.tamanio_cuadro)

        self.render = Render(self.jugador, self.teclado, self.tamanio_cuadro)

    def __contenido_canvas(self):
        self.dibujado_objetos = []
        objtest = {"solido": False, "tipo": "Suelo", "accion": 0}
        self.render.registrar(
            Suelos(objtest, "suelo", self.manejadorSprites.get_objetos(1), [0, 0]))
        self.render.registrar(
            Suelos(objtest, "suelo", self.manejadorSprites.get_objetos(2), [0, 2]))
        self.render.registrar(
            Suelos(objtest, "suelo", self.manejadorSprites.get_objetos(3), [0, 3]))
        self.render.registrar(
            Suelos(objtest, "suelo", self.manejadorSprites.get_objetos(5), [0, 4]))
        self.render.registrar(
            Suelos(objtest, "suelo", self.manejadorSprites.get_objetos(5), [0, 5]))
        self.render.registrar(
            Suelos(objtest, "suelo", self.manejadorSprites.get_objetos(5), [0, 6]))
        self.render.registrar(
            Suelos(objtest, "suelo", self.manejadorSprites.get_objetos(5), [0, 7]))
        self.render.registrar(
            Suelos(objtest, "suelo", self.manejadorSprites.get_objetos(5), [0, 8]))

    def _cerrar_teclado(self, *args):
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
        self.render.actualizar(self.tamanio_cuadro, dt)

    def dibujar(self, *dt):
        self.size = Window.size
        self.maya.canvas.clear()
        self.render.dibujar(self.maya.canvas, dt)
        self.jugador.dibujar(self.maya.canvas, self.tamanio_cuadro,self.tamanio_cuadro, dt)
