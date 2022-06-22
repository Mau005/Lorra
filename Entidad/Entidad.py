from abc import abstractmethod

class Entidad():

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

    @abstractmethod
    def actualizar(self, *dt):
        pass

    @abstractmethod
    def dibujar(self, *dt):
        pass