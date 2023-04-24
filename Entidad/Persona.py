from Entidad.Entidad import Entidad
from kivy.graphics import Rectangle

from Sprites.Animacion import Animacion


class Persona(Entidad):

    def __init__(self, manejadorsprite, nombre, vestimenta, pos, size):
        super().__init__(pos, size)
        self.manejadorsprite = manejadorsprite

        self.nombre = nombre
        self.velocidad_inicial = 1
        self.vestimenta = vestimenta
        self.animacion = Animacion(self.manejadorsprite.get_vestimenta(self.vestimenta))
        self.direccion = "derecha"
        self.enMovimiento = False
        self.bg = Rectangle(source=self.animacion.get_sprite(), size=size)

    def caminar(self, mover, direccion, dt):
        velocidad = self.velocidad_inicial * dt[0]
        self.direccion = direccion
        self.enMovimiento = True
        if direccion == "norte":
            mover.pos[1] -= velocidad
        elif direccion == "sur":
            mover.pos[1] += velocidad
        elif direccion == "izquierda":
            mover.pos[0] += velocidad
        elif direccion == "derecha":
            mover.pos[0] -= velocidad


    def __str__(self):
        return super().__str__() + f" Class: Persona"

    def actualizar(self, *dt):
        self.bg.pos = self.pos

    def dibujar(self, canvas, size_bg, pos_bg, dt):
        self.size = size_bg
        self.bg.size = self.size
        self.bg.pos = pos_bg
        self.bg.source = self.animacion.get_sprite()
        self.animacion.dibujar(self.enMovimiento, dt, direccion=self.direccion)
        canvas.add(self.bg)
