import mysql.connector

class Connection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        if self.connection.is_connected():
            print("Conexión exitosa")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Desconexión")

    def leer_LecturasTemperatura(self):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = "SELECT * FROM LecturasTemperatura"
                cursor.execute(query)
                Lecturas = cursor.fetchall()
                cursor.close()
                return Lecturas
            else:
                print("No se pudo conectar a la base de datos")
        except mysql.connector.Error as error:
            print("Error al leer LecturasTemperatura:", error)

    def ingresar_LecturasTemperatura(self, lectura_id, fecha_hora, temperatura):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = "INSERT INTO LecturasTemperatura (lectura_id, fecha_hora, temperatura) VALUES (%s, %s, %s)"
                values = (lectura_id, fecha_hora, temperatura)
                cursor.execute(query, values)
                self.connection.commit()
                cursor.close()
                print("Datos insertados correctamente")
            else:
                print("No se pudo conectar a la base de datos")
        except mysql.connector.Error as error:
            print("Error al ingresar LecturasTemperatura", error)
            
    def modificar_LecturasTemperatura(self, Ilectura_id, nueva_temperatura):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = "UPDATE LecturasTemperatura SET temperatura = %s WHERE lectura_id = %s"
                values = (nueva_temperatura, Ilectura_id)
                cursor.execute(query, values)
                self.connection.commit()
                cursor.close()
                print("Datos modificados correctamente")
            else:
                print("No se pudo conectar a la base de datos")
        except mysql.connector.Error as error:
            print("Error al modificar LecturasTemperatura", error)

    def eliminar_LecturasTemperatura(self, lectura_id):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = "DELETE FROM LecturasTemperatura WHERE lectura_id = %s"
                values = (lectura_id,)
                cursor.execute(query, values)
                self.connection.commit()
                cursor.close()
                print("Datos eliminados correctamente")
            else:
                print("No se pudo conectar a la base de datos")
        except mysql.connector.Error as error:
            print("Error al eliminar LecturasTemperatura", error)