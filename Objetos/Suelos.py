from Objetos.Objetos import Objetos


class Suelos(Objetos):

    def __init__(self,datos, nombre, sprite, pos, size):
        super().__init__(nombre, sprite, pos, size)
        self.solido = datos.get("solido")
        self.tipo = datos.get("tipo")
        self.accion = datos.get("accion_id")
