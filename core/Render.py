from Entidad.Entidad import Entidad
from Entidad.Persona import Persona
from Objetos.Suelos import Suelos


class Render(Entidad):

    def __init__(self,jugador, teclado, tamanio_cuadro):
        super().__init__([0, 0], [0, 0])
        """
        Sistema de capas de renderizado
        capa 1 (agua y suelos), capa 2 (bordes), capa 3(efectos)
        capa 4 (personas), capa5 (personas mas grandes con distancia)
        capa 5 (superior) ....
        """
        self.jugador = jugador
        self.teclado = teclado
        self.__renderizado = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8:[]}
        self.cambios_canvas = False
        self.tamanio_cuadro = tamanio_cuadro

    def movimiento_jugador(self, mover, dt):
        if self.teclado.get_tecla(119):
            self.jugador.caminar(mover, "norte", dt)
        elif self.teclado.get_tecla(115):
            self.jugador.caminar(mover, "sur", dt)
        elif self.teclado.get_tecla(97):
            self.jugador.caminar(mover, "izquierda", dt)
        elif self.teclado.get_tecla(100):
            self.jugador.caminar(mover, "derecha", dt)


    def registrar(self, obj):
        if isinstance(obj, Persona):
            self.__renderizado[4].append(obj)
        elif isinstance(obj, Suelos):
            self.__renderizado[1].append(obj)

    def actualizar(self, tamanio_cuadro, dt):
        self.tamanio_cuadro = tamanio_cuadro
        for capas in range(1, len(self.__renderizado.values()) + 1):
            for elementos in self.__renderizado[capas]:
                self.movimiento_jugador(elementos, dt)
                elementos.actualizar(dt)

    def dibujar(self, canvas, dt):
        for capas in range(1, len(self.__renderizado.values()) + 1):
            for elementos in self.__renderizado[capas]:
                elementos.dibujar(canvas, self.tamanio_cuadro, dt)

if __name__ == "__main__":
    test = Render()

    test.dibujar(1,1)