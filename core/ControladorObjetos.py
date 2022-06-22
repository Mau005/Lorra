from core.Herramientas import Herramientas

class ControladorObjetos:

    def __init__(self, path=None):
        if path is None:
            self.__datos = Herramientas.cargar_json("Data\Objetos\objetos.json")
        else:
            self.__datos = Herramientas.cargar_json(path)


    def get_objeto(self, idObjeto):
        """
        Devolvera los datos ingresados desde el objeto json
        se convierte a str para poder obtener la informacion correpsondiente
        :param idObjeto:
        :return:
        """
        return self.__datos[str(idObjeto)]

    def get_all(self):
        return self.__datos


if __name__ == "__main__":
    from pathlib import Path
    test = ControladorObjetos(path = Path(r"C:\Users\mpino\PycharmProjects\Lorra\Data\Objetos\objetos.json"))
    print(test.get_objeto(1))