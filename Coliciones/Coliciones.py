from Entidad.Entidad import Entidad


class Coliciones(Entidad):


    def __init__(self, pos, size, tag=None):
        super().__init__(pos, size)
        self.__tag = None
        self.circulo = None
        self.rectanulo = None
        self.set_tag(tag)

    def set_tag(self, tag):
        self.__tag = tag

    def get_tag(self, tag):
        return self.__tag

    def actualizar(self, objeto, *dt):
        pass

    def dibujar(self, *dt):
        pass