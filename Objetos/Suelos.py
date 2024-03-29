from Objetos.Objetos import Objetos
from Coliciones.Coliciones import Coliciones

class Suelos(Objetos):

    def __init__(self,datos, nombre, sprite, pos):
        super().__init__(nombre, sprite, pos)
        self.solido = datos.get("solido")
        self.tipo = datos.get("tipo")
        self.accion = datos.get("accion_id")
        self.colicion = Coliciones(self.pos, self.size)

    def __str__(self):
        return super().__str__() + f" Class: Suelos"

    def actualizar(self, dt):
        super().actualizar(dt)
        self.colicion.actualizar(self.pos, self.size, dt)
