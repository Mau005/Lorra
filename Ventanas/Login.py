from kivy.lang import Builder

from Ventanas.AbstractScreen import AbstractScreen

Builder.load_file("Ventanas/Login.kv")

class Login(AbstractScreen):
    def __init__(self, **kargs):
        super().__init__(**kargs)

    def next(self, name, *args):
        super().next(name)
    def actualizar(self, *dt):
        pass

    def dibujar(self, *dt):
        pass

    def ingresar(self, cuenta, passw):
        pass
