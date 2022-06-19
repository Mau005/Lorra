import datetime
class Querys:

    @classmethod
    def solicitar_ingreso(cls, nombre, password):
        querys = f"SELECT * FROM account WHERE nombre = {nombre} and pass = {password};"

    @classmethod
    def registrar_cuenta(cls, nombre, password):
        querys = f'INSERT INTO account VALUES("{nombre}", SHA("{password}"), "{datetime.date.today()}");'

if __name__ == "__main__":
    print()