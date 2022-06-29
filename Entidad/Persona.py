from Entidad.Entidad import Entidad
from kivy.graphics import Rectangle
from kivy.vector import Vector

from Sprites.Animacion import Animacion


class Persona(Entidad):

    # def __init__(self, manejadorsprite, nombre, email, vocacion, experiencia,
    #             sexo, hp_max, hp, mana_max, mana, puntos, vestimenta, posicion,
    #             acceso, pos, size):
    def __init__(self, manejadorsprite, nombre, vestimenta, posX, posY, posZ, pos, size):
        super().__init__(pos, size)

        self.pos_mapa = Vector((posX, posY, posZ))
        self.posX = posX
        self.posY = posY
        self.posZ = posZ
        self.manejadorsprite = manejadorsprite
        self.nombre = nombre
        self.vestimenta = vestimenta
        self.velocidad_inicial = 120
        self.animacion = Animacion(self.manejadorsprite.get_vestimenta(self.vestimenta))
        self.direccion = "derecha"
        self.enMovimiento = False
        self.bg = Rectangle(source=self.animacion.get_sprite(), pos=pos, size=size)

    def editor(self,direccion):
        if direccion == "norte":
            self.posY += 1
        elif direccion == "sur":
            self.posY -= 1
        elif direccion == "izquierda":
            self.posX -= 1
        elif direccion == "derecha":
            self.posX += 1

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

    def actualizar(self, *dt):
        self.bg.pos = self.pos

    def dibujar(self, canvas, size, *dt):
        self.size = size
        self.bg.size = self.size
        self.animacion.dibujar(self.enMovimiento, dt, direccion=self.direccion)
        self.bg.source = self.animacion.get_sprite()
        canvas.add(self.bg)
