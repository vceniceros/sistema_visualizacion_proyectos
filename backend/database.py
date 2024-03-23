import mysql.connector    

class  Database:
    #PRE:
    #POST: constructor
    def __init__(self, usuario, clave, bd, host, port):
        self.host = host
        self.port = port
        self.usuario = usuario
        self.clave = clave
        self.bd = bd
        self.connection = None
        
    #PRE: debe existir el host y la base de datos
    #POST: conecta con la base de datos
    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                port = self.port,
                user = self.usuario,
                password = self.clave,
                database = self.bd
            )
            print("conexion exitosa")
        except mysql.connector.Error as err:
            print("error al conectar a la base de datos: ",err)
            
    #PRE: se esta conectado a la base de datos
    #POST: se desconecta de la base de datos 
    def desconectar(self):
         if self.connection:
            self.connection.close()
            print("Conexión a MySQL cerrada correctamente")
         else:
            print("No hay conexión activa para cerrar")
    
    #PRE:
    #POST: ejecutar la linea
    def execute_query(self, query):
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
        usuario = 'root'
        clave = 'toor'
        bd = 'svpi'
        host = 'localhost'
        port = '3306'

        db = Database(usuario, clave, bd, host, port)


        db.conectar()

    
        db.desconectar()

        db.conectar() 
        resultados = db.execute_query('SELECT * FROM proyectos')
        for resul in resultados:
            print(resul)
        
        db.desconectar()

#test_mySql()