from Entidad.Entidad import Entidad
from kivy.graphics import Rectangle

from Sprites.Animacion import Animacion


class Persona(Entidad):

    def __init__(self, manejadorsprite, nombre, email, vocacion, experiencia,
                 sexo, hp_max, hp, mana_max, mana, puntos, vestimenta, posicion,
                 acceso, pos, size):
        super().__init__(pos, size)
        self.manejadorsprite = manejadorsprite

        self.nombre = nombre
        self.email = email
        self.vocacion = vocacion
        self.experiencia = experiencia
        self.velocidad_inicial = 80
        self.sexo = sexo
        self.hp_max = hp_max
        self.hp = hp
        self.mana_max = mana_max
        self.mana = mana
        self.puntos = puntos
        self.vestimenta = vestimenta
        self.posicion = posicion
        self.acceso = acceso
        self.animacion = Animacion(self.manejadorsprite.get_vestimenta(self.vestimenta))
        self.direccion = "derecha"
        self.enMovimiento = False
        self.bg = Rectangle(source=self.animacion.get_sprite(), pos=pos, size=size)

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

    def actualizar(self, teclado,*dt):
        self.bg.pos = self.pos

    def dibujar(self, canvas, *dt):
        self.animacion.dibujar(self.enMovimiento, dt, direccion=self.direccion)
        self.bg.source = self.animacion.get_sprite()
        canvas.add(self.bg)
