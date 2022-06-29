from core.Herramientas import Herramientas
from Objetos.Suelos import Suelos

class ControladorObjetos:

    def __init__(self, manejadorSprites, path=None):
        self.manejadorSprites = manejadorSprites
        if path is None:
            self.__datos = Herramientas.cargar_json("Data/Objetos/objetos.json")
        else:
            self.__datos = Herramientas.cargar_json(path)

    def get_objeto(self, idObjeto, pos , size):
        """
        Devolvera los datos ingresados desde el objeto json
        se convierte a str para poder obtener la informacion correpsondiente
        :param idObjeto:
        :return:
        """
        datos = self.__datos[str(idObjeto)]

        if datos.get("tipo") == "Suelo":
            return Suelos(datos,self.manejadorSprites.get_objetos(int(idObjeto)), pos, size)

        return None

    def get_all(self):
        return self.__datos


if __name__ == "__main__":
    from pathlib import Path
    test = ControladorObjetos(path = Path(r"C:\Users\mpino\PycharmProjects\Lorra\Data\Objetos\objetos.json"))
    print(test.get_objeto(1))