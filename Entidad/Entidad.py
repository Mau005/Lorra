from abc import ABC, abstractmethod


class Entidad(ABC):

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

    @abstractmethod
    def actualizar(self, *dt):
        pass

    @abstractmethod
    def dibujar(self, *dt):
        pass
