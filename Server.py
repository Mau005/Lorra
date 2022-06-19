import socket
from core.Constantes import *
from Networks.Hilo_Servidor import Hilo_Servidor
from BaseDatos.Querys import Querys

class Server:

    def __init__(self):
        self.__configurarServidor()

        self.querys = Querys()

    def __configurarServidor(self):
        self.socket = socket.socket()
        self.socket.bind((IP, PORT))
        self.socket.listen(5)
        self.enFuncionamiento = True
        self.lista_con = []

    def iniciar(self):
        print("[OK] Servidor Online")
        while self.enFuncionamiento:
            clt, addr = self.socket.accept()
            objeto = Hilo_Servidor(clt, addr)
            self.lista_con.append(objeto)
            objeto.start()


        self.cerrar()

    def cerrar(self):
        self.socket.close()



if __name__ == "__main__":
    Server().iniciar()
