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

    def actualizar(self, teclado,*dt):
        pass

    def dibujar(self, canvas, *dt):
        self.animacion.set_direccion(self.direccion)
        self.animacion.dibujar(self.enMovimiento, dt)
        self.bg.source = self.animacion.get_sprite()
        self.bg.pos = self.pos
        canvas.add(self.bg)
