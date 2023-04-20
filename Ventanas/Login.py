
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen


class MDCardPre(MDCard, CommonElevationBehavior):
    pass
class Login(MDScreen):
    def __init__(self, **kargs):
        super().__init__(**kargs)

    def next(self, name, *args):
        print(f"Que estoy pasando: {name}")
        self.manager.current = name
    def actualizar(self, *dt):
        pass

    def dibujar(self, *dt):
        pass

    def ingresar(self, cuenta, passw):
        pass
