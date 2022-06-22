from Entidad.Entidad import Entidad


class Coliciones(Entidad):


    def __init__(self, pos, size, tag=None):
        super().__init__(pos, size)
        self.__tag = None
        self.circulo = None
        self.rectangulo = size
        self.set_tag(tag)

    def get_colicion(self):
        return self.rectangulo

    def chequear_colicion(self, objeto):
        colicion = objeto.get_colicion()
        pos = self.pos
        if colicion[0] + pos[0] <= self.pos[0] <= colicion[0] - pos[0] and self.pos[1] >= colicion[1] + pos[1] and self.ps[1] <= colicion[1] - pos[1]:
            return True

        return False

    def set_tag(self, tag):
        self.__tag = tag

    def get_tag(self, tag):
        return self.__tag

    def actualizar(self, *dt):
        pass

    def dibujar(self, *dt):
        pass