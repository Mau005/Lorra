from Sprites.Animacion import Animacion
from kivy.graphics import Rectangle
from Entidad.Entidad import Entidad

class Objetos(Entidad):

    def __init__(self, nombre, sprite, pos, size):
        super().__init__(pos, size)
        self.nombre = nombre
        self.sprite = sprite
        self.animacion = Animacion(sprite)
        if len(self.sprite.get("sur")) >= 2:
            self.enMovimiento = True
            self.bg = Rectangle(source=self.animacion.ruta_predefinida, pos = pos, size = size)
        else:
            self.enMovimiento = False
            self.bg = Rectangle(source=self.animacion.ruta_sprite, pos = pos, size = size)





    def actualizar(self, dt):
        self.animacion.actualizar(dt)
        self.bg.pos = self.pos


    def dibujar(self, canvas, size, dt):
        self.bg.size = size
        if self.enMovimiento:
            self.animacion.dibujar(self.enMovimiento, dt)
            self.bg.source = self.animacion.ruta_predefinida

        canvas.add(self.bg)
