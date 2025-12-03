import mysql.connector

class ConexionBD:
    def __init__(self):
        self.conexion = None
        self.cursor = None
        self._inicializar_conexion()

    def _inicializar_conexion(self):
        try:
            self.conexion = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="bd_notas"
            )
            self.cursor = self.conexion.cursor(buffered=True)
        except Exception as e:
            print("Error al conectar con la base de datos:", e)
    
    def ejecutar(self, sql, valores=None):
        try:
            self.cursor.execute(sql, valores)
            self.conexion.commit()
            return True
        except Exception as e:
            print("Error al ejecutar consulta:", e)
            return False
    
    def consultar(self, sql, valores=None):
        self.cursor.execute(sql, valores)
        return self.cursor.fetchall()
    
    def cerrar_conexion(self):
        if self.conexion:
            self.cursor.close()
            self.conexion.close()