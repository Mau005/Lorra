from abc import ABC, abstractmethod


class Entidad(ABC):

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

    @abstractmethod
    def actualizar(self, *dt):
        pass

    def __str__(self):
        return f"Posicion: {self.pos}"

    @abstractmethod
    def dibujar(self, canvas, size_bg, pos_bg, dt):
        pass
