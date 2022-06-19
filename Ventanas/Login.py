from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file("Ventanas/Login.kv")

class Login(Screen):
    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.name = "login"

    def actualizar(self, *dt):
        pass

    def dibujar(self, *dt):
        pass

    def ingresar(self, cuenta, passw):
        pass
