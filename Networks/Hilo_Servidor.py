from threading import Thread

class Hilo_Servidor(Thread):

    def __init__(self, clt, addr):
        super().__init__(self)
        self.cliente = clt
        self.addr = addr

    def run(self):
        while True:
            pass

    def solicitar_ingreso(self):
        pass