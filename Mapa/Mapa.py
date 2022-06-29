import numpy as np


class Mapa():

    def __init__(self, max_x, max_y, max_z):
        self._mapa = np.zeros((max_x, max_y, max_z), dtype=int)

        for y in range(0, 10):
            for x in range(0, 4):
                self.set_pos(x,y,0,5)

        if max_x >= 200:

            for y in range(100, 200):
                for x in range(100,200):
                    self.set_pos(x,y,0,5)

    def get_mapa(self):
        """
        MEthodo DEPRECATED DEBE CAMBIAR SI O SI NO PUEDE QUEDAR ASI FDOP
        :return: el mapa
        """
        return self._mapa


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

    print(map.get_pos(10,10,0))
