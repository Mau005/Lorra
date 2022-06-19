import mysql.connector
import sys

from core.Herramientas import Herramientas


class ConectarBD:

    def __init__(self):
        configuracion_servidor = Herramientas.cargar_json("ServerConfiguracion.json")
        self.contenidoBD = configuracion_servidor["Mysql"]
        self.bd = None
        self.cursor = None
        self.cifrado = None
        self.__conectar()
        self.cerrar()
        print("[OK] Conectado con exito al Servidor Mysql")

    def __conectar(self):
        try:
            self.bd = mysql.connector.connect(
                user=self.contenidoBD.get("UsuarioBD"),
                password=self.contenidoBD.get("PasswordBD"),
                database=self.contenidoBD.get("DataBase"),
                host=self.contenidoBD.get("HostBD"),
                port=self.contenidoBD.get("PortBD"),
            )
            self.cifrado = self.contenidoBD.get("Cifrado")
            self.cursor = self.bd.cursor()

        except mysql.connector.Error as error:
            print(f"[CRITICAL] Error BD: {error}")
            sys.exit(0)

    def registrar(self, querys):
        self.__conectar()
        self.cursor.execute(querys)
        self.bd.commit()
        self.cerrar()

    def solicitar(self, querys, cantidad):
        self.__conectar()
        self.cursor.execute(querys)
        if cantidad == 1:
            contenido = self.cursor.fetchone()
        elif cantidad >= 2:
            contenido = self.cursor.fetchall()
        self.cerrar()
        return contenido

    def cerrar(self):
        self.bd.close()
        self.cursor.close()
