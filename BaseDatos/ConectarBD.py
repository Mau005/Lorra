from mysql.connector import MySQLConnection

class ConectarBD:

    def __init__(self):
        self.bd = MySQLConnection.connect(
            user = "",
            password = "",
            database = "",
            host = "",
            port = "",
        )