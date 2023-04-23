from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.screenmanager import MDScreenManager

from Ventanas.Juego import Juego
from Ventanas.Login import Login
from core.Constantes import FPS



class Lorra(MDApp):
    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.manejador = MDScreenManager()
        self.manejador.add_widget(Login(name="login"))
        self.manejador.add_widget(Juego(name="juego"))

        Clock.schedule_interval(self.actualizar, 1/FPS)
        Clock.schedule_interval(self.dibujar, 1 / FPS)

    def actualizar(self, *dt):
        for names in self.manejador.screen_names:
            self.manejador.get_screen(names).actualizar(dt[0])

    def dibujar(self, *dt):
        for names in self.manejador.screen_names:
            self.manejador.get_screen(names).dibujar(dt[0])


    def build(self):
        return self.manejador


if __name__ == "__main__":
    Lorra().run()
