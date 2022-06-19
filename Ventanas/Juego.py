from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.graphics import Rectangle
from Entidad.Persona import Persona
from Sprites.ManejadorSprites import ManejadorSprites


class Juego(MDScreen):
    def __init__(self, window_size,**kargs):
        super().__init__(size = window_size, **kargs)
        print(f"Size: {self.size} Size_Hint: {self.size_hint}")
        self.name = "Juego"
        self.maya = MDFloatLayout(size = self.size, size_hint = self.size_hint)
        self.add_widget(self.maya)
        self.manejadorSprites = ManejadorSprites()

        self.jugador = Persona(self.manejadorSprites.get_vestimenta(2), 32,self.maya.pos, self.maya.size)

        with self.maya.canvas.before:
            self.bg = Rectangle(size = [32,32])




    def actualizar(self, *dt):
        self.jugador.actualizar(dt)

    def dibujar(self, window_size, *dt):
        self.size = window_size
        self.maya.canvas.clear()
        self.jugador.dibujar(self.maya.canvas, dt)
