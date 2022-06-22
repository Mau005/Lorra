import numpy as np


class Mapa():

    def __init__(self, max_x, max_y, max_z):
        self._mapa = np.zeros((max_x, max_y, max_z), dtype=int)

    def get_pos(self, x, y, z):
        return self._mapa[x][y][z]

    def extracto_mapa(self, pos):
        return self._mapa

    def set_pos(self, x, y, z, valor):
        self._mapa[x][y][z] = valor

    def info(self):
        return self._mapa


if __name__ == "__main__":
    map = Mapa(100, 100, 5)
    print(len(map.info()[0][0]))

    print(map.get_pos(10,10,2))
