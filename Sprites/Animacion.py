from Entidad.Entidad import Entidad
from core.Constantes import VELOCIDAD_RECORRE_FPS, VELOCIDAD_FPS

class Animacion(Entidad):

    def __init__(self, sprite):
        self.sprite = sprite
        self.ruta_sprite = self.sprite["ruta"]

        self.ruta_predefinida = f"{self.ruta_sprite}{self.sprite['sur'][0]}"
        self.direccion = "sur"
        self.fps_actual = 0
        self.cuadro_por_segundo = VELOCIDAD_FPS
        self.control_tiempo = 0.0

    def get_sprite(self):
        return self.ruta_predefinida

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        if direccion == "sur" or direccion == "norte" or direccion == "izquierda" or direccion == "derecha":
            self.direccion = direccion

    def dibujar(self,enMovimiento, *dt):
        """
        Methodo realizado para operar la informacion de la secuencia de imagenes
        :param dt: tiempo transcurrido
        :return:  nothings
        """
        if enMovimiento:
            self.ruta_predefinida = f"{self.ruta_sprite}{self.sprite[self.direccion][self.fps_actual]}"

            if self.fps_actual >= len(self.sprite[self.direccion]) - 1:
                self.fps_actual = -1

            if self.control_tiempo >= self.cuadro_por_segundo:
                self.fps_actual += 1
                self.control_tiempo = 0.0

            self.control_tiempo += VELOCIDAD_RECORRE_FPS
        else:
            self.ruta_predefinida = f"{self.ruta_sprite}{self.sprite[self.direccion][0]}"



if __name__ == "__main__":
    test = {'norte': [1, 2, 3, 4, 5, 6, 7, 8],
            'derecha': [9, 10, 11, 12, 13, 14, 15, 16],
            'izquierda': [17, 18, 19, 20, 21, 22, 23, 24],
            'sur': [25, 26, 27, 28, 29, 30, 31, 32],
            'ruta': 'atlas://Assets/RPG CHARACTERS/Aguy.atlas/'}
    anim = Animacion(test)
    while True:
        anim.dibujar(2)

