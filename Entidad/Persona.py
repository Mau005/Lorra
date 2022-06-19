from Entidad.Entidad import Entidad
from kivy.graphics import Rectangle

from Sprites.Animacion import Animacion


class Persona(Entidad):

    def __init__(self, sprite, rango, pos, size):
        super().__init__(pos, size)
        self.animacion = Animacion(sprite)
        self.direccion = "sur"
        self.enMovimiento = True
        self.bg = Rectangle(source=self.animacion.get_sprite(), pos=pos, size=size)

    def actualizar(self, *dt):
        pass

    def dibujar(self, canvas, *dt):
        self.animacion.set_direccion(self.direccion)
        self.animacion.dibujar(self.enMovimiento,dt)
        self.bg.source = self.animacion.get_sprite()
        canvas.add(self.bg)

