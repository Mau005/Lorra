from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock

from Ventanas.Juego import Juego
from Ventanas.Login import Login
from core.Constantes import FPS



class Lorra(MDApp):
    def __init__(self, **kargs):
        super().__init__(**kargs)

        self.manejador = ScreenManager()
        self.login = Login()
        self.juego = Juego()

        #self.manejador.add_widget(self.login)
        self.manejador.add_widget(self.juego)
        Clock.schedule_interval(self.actualizar, 1/FPS)
        Clock.schedule_interval(self.dibujar, 1 / FPS)

    def actualizar(self, *dt):
        self.juego.actualizar(dt)

    def dibujar(self, *dt):
        self.juego.dibujar(*dt) #Deprectad a futuro


    def build(self):
        return self.manejador


if __name__ == "__main__":
    Lorra().run()
