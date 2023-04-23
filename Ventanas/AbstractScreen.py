from kivy.uix.screenmanager import Screen


class AbstractScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def next(self, name):
        self.manager.current = name

    def actualizar(self,*dt):
        pass

    def dibujar(self, *dt):
        pass
