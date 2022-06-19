import socket
from core.Constantes import *
from Cifrado.Cifrado import Cifrados


class Hilo_Cliente():
    def __init__(self):
        self.socket = self.__conectar_socket()


    def __conectar_socket(self):
        try:
            self.socket = socket.socket()
            self.socket.connect((IP, PORT))
            return self.socket
        except socket.error as error:
            print(error)
            return None

    def enviar(self, data):
        self.socket.send(Cifrados.empaquetar(data))
        return self.recibir()

    def recibir(self):
        return Cifrados.desenpaqueta(self.socket.recv(CANTIDAD_PAQUETES))
