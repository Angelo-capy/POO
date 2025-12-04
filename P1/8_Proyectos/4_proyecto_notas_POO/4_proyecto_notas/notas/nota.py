from conexionBD import ConexionBD

class Nota:
    def __init__(self):
        self.db = ConexionBD()
    
    def crear(self, usuario_id, titulo, descripcion):
        sql = "INSERT INTO notas (usuario_id, titulo, descripcion) VALUES (%s, %s, %s)"
        valores = (usuario_id, titulo, descripcion)
        return self.db.ejecutar(sql, valores)
    
    def mostrar(self, usuario_id):
        sql = "SELECT id, usuario_id, titulo, descripcion, fecha FROM notas WHERE usuario_id = %s ORDER BY fecha DESC"
        valores = (usuario_id,)
        return self.db.consultar(sql, valores)
    
    def cambiar(self, id_nota, titulo, descripcion):
        sql = "UPDATE notas SET titulo = %s, descripcion = %s WHERE id = %s"
        valores = (titulo, descripcion, id_nota)
        return self.db.ejecutar(sql, valores)
    
    def borrar(self, id_nota):
        sql = "DELETE FROM notas WHERE id = %s"
        valores = (id_nota,)
        return self.db.ejecutar(sql, valores)
    
    def obtener_por_id(self, id_nota, usuario_id):
        sql = "SELECT id, usuario_id, titulo, descripcion, fecha FROM notas WHERE id = %s AND usuario_id = %s"
        valores = (id_nota, usuario_id)
        resultado = self.db.consultar(sql, valores)
        return resultado[0] if resultado else None

# Instancia global para mantener compatibilidad
nota = Nota()