import socket
from core.Constantes import *
from Networks.Hilo_Servidor import Hilo_Servidor

class Server:

    def __init__(self):
        self.socket = socket.socket((IP, PORT))
        self.socket.bind((5))
        self.enFuncionamiento = True
        self.lista_con = []

    def iniciar(self):
        while self.enFuncionamiento:
            clt, addr = self.socket.accept()
            objeto = Hilo_Servidor(clt,addr)
            self.lista_con.append(objeto)
            objeto.start()


        self.cerrar()

    def cerrar(self):
        self.socket.close()



if __name__ == "__main__":
    Server().iniciar()
