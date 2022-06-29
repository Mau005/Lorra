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

    def registrar_mapa(self, *args):
        for elementos in args:
            self.registrar(elementos)

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

    def actualizar_editor(self, dt):
        self.movimiento_editor(dt)


    def movimiento_editor(self, dt):
        if self.teclado.get_tecla(119):
            self.jugador.posY +=1
        elif self.teclado.get_tecla(115):
            self.jugador.posY -=1
        elif self.teclado.get_tecla(97):
            self.jugador.posX -=1
        elif self.teclado.get_tecla(100):
            self.jugador.posX += 1


    def dibujar_editor(self, mapa, controladorObjeto):
        x_j = self.jugador.posX
        y_j = self.jugador.posY
        self.__renderizado = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
        for y in range(0, 100):
            for x in range(0,100):
                for z in range(0, 4):
                    print(x * 32, y * 32, z)
                    try:
                        contenido = mapa[x][y][z]
                    except IndexError:
                        continue
                    pos = [x * 32, y * 32]
                    if contenido >= 1:
                        self.registrar(controladorObjeto.get_objeto(contenido, pos, [32,32]))

    def dibujar(self, canvas, dt):
        canvas.clear()
        for capas in range(1, len(self.__renderizado.values()) + 1):
            for elementos in self.__renderizado[capas]:
                elementos.dibujar(canvas, self.tamanio_cuadro, dt)

if __name__ == "__main__":
    test = Render()

    test.dibujar(1,1)