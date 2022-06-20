

class Teclado():

    def __init__(self):
        """
        Clase creada para poder realizar una simulacion de teclado en tiempo real
        por el retardo del evento de accion.
        """
        self.__teclado = [False for x in range(1, 400)]

    def precionar_tecla(self, key):
        self.__teclado[key] = True

    def soltar_tecla(self, key):
        self.__teclado[key] = False

    def get_tecla(self, key):
        return self.__teclado[key]

    def check(self):
        for arg in self.__teclado:
            pass


if __name__ == "__main__":
    teclado = Teclado()
    teclado.check()