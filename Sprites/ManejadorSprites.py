class ManejadorSprites:

    def __init__(self):
        self.secuencia = {1: {"norte": [1, 2, 3, 4, 5, 6, 7, 8],
                              "derecha": [9, 10, 11, 12, 13, 14, 15, 16],
                              "izquierda": [17, 18, 19, 20, 21, 22, 23, 24],
                              "sur": [25, 26, 27, 28, 29, 30, 31, 32]},
                          2: {"sur": [1, ]},
                          3: {"sur": [1, 2, 3, 4, 5, 6, 7, 8]}

                          }
        self.vestimentas = {1: {"ruta": "atlas://Assets/RPG CHARACTERS/Aguy.atlas/",
                                "secuencia": 1},
                            2: {"ruta": "atlas://Assets/RPG CHARACTERS/Child.atlas/",
                                "secuencia": 1}
                            }

        self.objetos = {1: {"ruta": "atlas://Assets/Enviroment/enviroment1.atlas/1",
                            "secuencia": 2},
                        2: {"ruta": "atlas://Assets/Enviroment/enviroment1.atlas/2",
                            "secuencia": 2},
                        3: {"ruta": "atlas://Assets/Enviroment/enviroment1.atlas/3",
                            "secuencia": 2},
                        4: {"ruta": "atlas://Assets/Enviroment/enviroment1.atlas/4",
                            "secuencia": 2},
                        5: {"ruta": "atlas://Assets/Agua/agua.atlas/",
                            "secuencia": 3}
                        }


    def get_objetos(self, id_objeto):
        """
        Ruta de objeto retorna la ruta del path donde se encuentra
        secuencia obtiene la secuencia de la animacion
        se updatea para devolver un diccionario
        :param id_objeto:
        :return: diccionario que devuelve la ruta y la sencuencia
        """
        ruta_objeto = self.objetos[id_objeto]["ruta"]
        secuencia = self.secuencia[self.objetos[id_objeto]["secuencia"]]
        secuencia.update({"ruta": ruta_objeto})
        return secuencia

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
    print(test.get_objetos(1))
