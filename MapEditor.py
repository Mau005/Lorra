
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.core.window import Window

from Controles.Teclado import Teclado
from Entidad.Persona import Persona
from Mapa.Mapa import Mapa
from Sprites.ManejadorSprites import ManejadorSprites
from core.ControladorObjetos import ControladorObjetos
from core.Render import Render

Builder.load_file("Ventanas/mapdeditor.kv")

class Contenido(MDScreen):
    maya = ObjectProperty()


    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.name = "contenido"
        self._teclado = Window.request_keyboard(self._cerrar_teclado, self, 'text')
        self.teclado = Teclado()
        self._teclado.bind(on_key_down=self._precionar_tecla)
        self._teclado.bind(on_key_up=self._soltar_tecla)
        self.cuadro = [32,32]


        self.configuracion_canvas()

    def configuracion_canvas(self):
        self.manejadorSprite = ManejadorSprites()
        self.jugador = Persona(self.manejadorSprite, "Mau",  1, 0,0,0,[0,0],[32,32])
        self.controladorObjetos = ControladorObjetos(self.manejadorSprite)
        self.render = Render(self.jugador, self.teclado, self.cuadro)
        self.mapa = Mapa(1000,1000,4)


    def on_touch_down(self, touch):
        x = touch.pos[0] / 32
        y = touch.pos[1] / 32
        print([int(x),int(y)])

    def on_touch_up(self, touch):
        x = touch.pos[0] / 32
        y = touch.pos[1] / 32
        print([int(x), int(y)])

    def _cerrar_teclado(self, *args):
        print("Se ha cerrado el teclado")
        self._teclado.unbind(on_key_down=self._precionar_tecla)
        self._teclado.unbind(on_key_up=self._soltar_tecla)
        self._teclado = None

    def _precionar_tecla(self, *args):
        self.teclado.precionar_tecla(args[1][0])

    def _soltar_tecla(self, *args):
        self.teclado.soltar_tecla(args[1][0])

    def actualizar(self, dt):
        self.render.actualizar_editor(dt)
        self.render.dibujar_editor(self.mapa.get_mapa(), self.controladorObjetos)


        self.render.dibujar(self.maya.canvas, dt)

    def prueba(self):
        print("estoy apretando")

class MapEditor(MDApp):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.manejador = ScreenManager()
        self.contenido = Contenido()
        self.manejador.add_widget(self.contenido)
        Clock.schedule_interval(self.actualizar, 1/60)


    def actualizar(self, *dt):
        self.contenido.actualizar(dt)

    def build(self):
        return self.manejador

if __name__ == "__main__":
    MapEditor().run()
