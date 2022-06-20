import datetime
from BaseDatos.ConectarBD import ConectarBD
class Querys:

    def __init__(self):
        self.conectorbd = ConectarBD()


    def solicitar_ingreso(self, nombre, password):
        querys = f'SELECT * FROM account WHERE EMAIL = "{nombre}" and PASS = "{password}";'
        return self.conectorbd.solicitar(querys, 1)
    def solicitar_ingreso_cifrado(self, nombre, password):
        querys = f'SELECT * FROM account WHERE EMAIL = "{nombre}" and PASS = SHA("{password}");'
        return self.conectorbd.solicitar(querys, 1)


    def registrar_cuenta(self, nombre, password):
        querys = f'INSERT INTO account VALUES("{nombre}", SHA("{password}"), "{datetime.date.today()}");'
        self.conectorbd.registrar(querys)

    def solicitar_jugador(self, email):
        querys = f'SELECT * FROM `player` WHERE EMAIL = "{email}";'
        #querys = f'SELECT * FROM player WHERE EMAIL = "{email}";'
        return self.conectorbd.solicitar(querys, 1)

    def registrar_skills(self, nombre):
        querys = f'INSERT INTO skills VALUES("{nombre}")'
        pass

if __name__ == "__main__":
    print()