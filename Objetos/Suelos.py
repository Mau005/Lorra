from Objetos.Objetos import Objetos
from Coliciones.Coliciones import Coliciones

class Suelos(Objetos):

    def __init__(self,datos, sprite, pos, size):
        super().__init__(datos.get("nombre"), sprite, pos, size)
        self.solido = datos.get("solido")
        self.tipo = datos.get("tipo")
        self.accion = datos.get("accion_id")
        self.colicion = Coliciones(self.pos, size)


    def actualizar(self, dt):
        super().actualizar(dt)
        self.colicion.actualizar(self.pos, self.size, dt)
