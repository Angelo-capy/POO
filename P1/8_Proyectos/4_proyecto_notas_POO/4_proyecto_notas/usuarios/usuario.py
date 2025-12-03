from conexionBD import ConexionBD
import hashlib

class Usuario:
    def __init__(self):
        self.db = ConexionBD()
    
    @staticmethod
    def _hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def registrar(self, nombre, apellidos, email, password):
        password_hash = self._hash_password(password)
        sql = "INSERT INTO usuarios (nombre, apellidos, email, password) VALUES (%s, %s, %s, %s)"
        valores = (nombre, apellidos, email, password_hash)
        
        return self.db.ejecutar(sql, valores)
    
    def iniciar_sesion(self, email, password):
        password_hash = self._hash_password(password)
        sql = "SELECT id, nombre, apellidos FROM usuarios WHERE email = %s AND password = %s"
        valores = (email, password_hash)
        
        resultado = self.db.consultar(sql, valores)
        if resultado:
            return resultado[0]  # Retorna (id, nombre, apellidos)
        return None
    
    def existe_email(self, email):
        sql = "SELECT id FROM usuarios WHERE email = %s"
        valores = (email,)
        resultado = self.db.consultar(sql, valores)
        return len(resultado) > 0

# Instancia global para mantener compatibilidad
usuario = Usuario()