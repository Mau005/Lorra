class ManejadorSprites:

    def __init__(self):
        self.secuencia = {1: {"norte": [1, 2, 3, 4, 5, 6, 7, 8],
                              "derecha": [9, 10, 11, 12, 13, 14, 15, 16],
                              "izquierda": [17, 18, 19, 20, 21, 22, 23, 24],
                              "sur": [25, 26, 27, 28, 29, 30, 31, 32]}
                          }
        self.vestimentas = {1: {"ruta": "atlas://Assets/RPG CHARACTERS/Aguy.atlas/",
                                "secuencia": 1},
                            2: {"ruta": "atlas://Assets/RPG CHARACTERS/Child.atlas/",
                                "secuencia": 1}
                            }

    def get_vestimenta(self, id_vestimenta):
        """
        Methodo utilizado para recojer la informacion de las vestimentas
        :param id_vestimenta: que recoje el id de la vestimenta
        :return: retorna un diccioanrio con la ruta y la secuencia de la animacion
        """
        ruta_vestimenta = self.vestimentas[id_vestimenta]["ruta"]
        secuencia = self.secuencia[self.vestimentas[id_vestimenta]["secuencia"]]
        secuencia.update({"ruta": ruta_vestimenta})
        return secuencia

if __name__ == "__main__":
    test = ManejadorSprites()
    print(test.get_vestimenta(1))
