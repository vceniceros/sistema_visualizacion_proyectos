import mysql.connector


class Database:

    def __init__(self, usuario, clave, bd, host, port):
        """
        PRE: recibe un usuario clave, base de datos, host y puerto como parametros
        POST: constructor
        """
        self.host = host
        self.port = port
        self.usuario = usuario
        self.clave = clave
        self.bd = bd
        self.connection = None

    def conectar(self):
        """PRE: debe existir el host y la base de datos
        POST: conecta con la base de dato"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.usuario,
                password=self.clave,
                database=self.bd,
            )
            print("conexion exitosa")
        except mysql.connector.Error as err:
            print("error al conectar a la base de datos: ", err)

    def desconectar(self):
        """PRE: se esta conectado a la base de datos
        POST: se desconecta de la base de datos"""
        if self.connection:
            self.connection.close()
            print("Conexión a MySQL cerrada correctamente")
        else:
            print("No hay conexión activa para cerrar")

    def execute_query(self, query):
        """
        PRE:
        POST: ejecutar la linea
        """

        cursor = self.connection.cursor()
        try:
            cursor.execute(query)

            results = cursor.fetchall()

            self.connection.commit()

            print("Consulta ejecutada correctamente")

            return results
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta: ", err)
            return None
        finally:
            cursor.close()

    def execute_query_values(self, query_and_values):
        """
        PRE:
        POST: ejecutar la linea
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(*query_and_values)

            results = cursor.fetchall()

            self.connection.commit()

            print("Consulta ejecutada con éxito")

            return results
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta: ", err)
            return None


def test_mySql():
    # Datos de conexión
    usuario = "root"
    clave = "toor"
    bd = "svpi"
    host = "localhost"
    port = "3306"

    db = Database(usuario, clave, bd, host, port)

    db.conectar()

    db.desconectar()

    db.conectar()
    resultados = db.execute_query("SELECT * FROM proyectos")
    for resul in resultados:
        print(resul)

    db.desconectar()


# test_mySql()
