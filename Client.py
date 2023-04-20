from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.screenmanager import MDScreenManager

from Ventanas.Juego import Juego
from Ventanas.Login import Login
from core.Constantes import FPS


Builder.load_file("Ventanas/Login.kv")

class Lorra(MDApp):
    def __init__(self, **kargs):
        super().__init__(**kargs)

        self.manejador = MDScreenManager()
        self.login = Login(name ="login")
        self.juego = Juego(name="juego")


        self.manejador.add_widget(self.juego)

        Clock.schedule_interval(self.actualizar, 1/FPS)
        Clock.schedule_interval(self.dibujar, 1 / FPS)

    def actualizar(self, *dt):
        self.juego.actualizar(dt[0])

    def dibujar(self, *dt):
        self.juego.dibujar(dt[0]) #Deprectad a futuro


    def build(self):
        return self.manejador


if __name__ == "__main__":
    Lorra().run()
