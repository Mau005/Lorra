import json
import os


class Herramientas:

    @classmethod
    def cargar_json(cls, path):
        archivo = open(path, encoding="utf-8")
        return json.load(archivo)

    @classmethod
    def comprobar_archivo(cls, ruta):
        return os.path.exists(ruta)


if __name__ == "__main__":
    from pathlib import Path

    test = Herramientas()
    print(test.cargar_json(Path(r"C:\Users\mpino\PycharmProjects\Lorra\ServerConfiguracion.json")))
    print(test.comprobar_archivo("Constantes.py"))
