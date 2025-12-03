import funciones
from usuarios import usuario
from notas import nota
import getpass

class SistemaNotas:
    def __init__(self):
        self.usuario_actual = None
    
    def ejecutar(self):
        opcion = True
        while opcion:
            funciones.borrarPantalla()
            opcion = funciones.menu_usurios()

            if opcion == "1" or opcion == "REGISTRO":
                self._registrar_usuario()
            elif opcion == "2" or opcion == "LOGIN":
                self._iniciar_sesion()
            elif opcion == "3" or opcion == "SALIR":
                self._salir_sistema()
                opcion = False
            else:
                self._opcion_invalida()
    
    def _registrar_usuario(self):
        funciones.borrarPantalla()
        print("\n \t ..:: Registro en el Sistema ::..")
        nombre = input("\t ¿Cual es tu nombre?: ").upper().strip()
        apellidos = input("\t ¿Cuales son tus apellidos?: ").upper().strip()
        email = input("\t Ingresa tu email: ").lower().strip()
        password = getpass.getpass("\t Ingresa tu contraseña: ").strip()
        
        resultado = usuario.registrar(nombre, apellidos, email, password)
        if resultado:
            print(f"\n\t {nombre} {apellidos}, se registro correctamente con el email: {email}")
        else:
            print(f"\n\t ...Por favor intentelo de nuevo, no fue posible registrar al usuario")
        funciones.esperarTecla()
    
    def _iniciar_sesion(self):
        funciones.borrarPantalla()
        print("\n \t ..:: Inicio de Sesión ::..")
        email = input("\t Ingresa tu E-mail: ").lower().strip()
        password = getpass.getpass("\t Ingresa tu contraseña: ").strip()
        
        registro = usuario.iniciar_sesion(email, password)
        if registro:
            self.usuario_actual = registro
            self._menu_notas(registro[0], registro[1], registro[2])
        else:
            print(f"\n\t E-mail y/o contraseña incorrectos, vuelva a intentarlo...")
            funciones.esperarTecla()
    
    def _menu_notas(self, usuario_id, nombre, apellidos):
        gestor_notas = GestorNotas(usuario_id, nombre, apellidos)
        gestor_notas.ejecutar()
    
    def _salir_sistema(self):
        print("Termino la Ejecución del Sistema")
        funciones.esperarTecla()
    
    def _opcion_invalida(self):
        print("Opcion no valida")
        funciones.esperarTecla()


class GestorNotas:
    def __init__(self, usuario_id, nombre, apellidos):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.apellidos = apellidos
    
    def ejecutar(self):
        while True:
            funciones.borrarPantalla()
            print(f"\n \t \t \t Bienvenido {self.nombre} {self.apellidos}, has iniciado sesión ...")
            opcion = funciones.menu_notas()

            if opcion == '1' or opcion == "CREAR":
                self._crear_nota()
            elif opcion == '2' or opcion == "MOSTRAR":
                self._mostrar_notas()
            elif opcion == '3' or opcion == "CAMBIAR":
                self._cambiar_nota()
            elif opcion == '4' or opcion == "ELIMINAR":
                self._eliminar_nota()
            elif opcion == '5' or opcion == "SALIR":
                break
            else:
                self._opcion_invalida_notas()
    
    def _crear_nota(self):
        funciones.borrarPantalla()
        print(f"\n \t .:: Crear Nota ::. ")
        titulo = input("\tTitulo: ")
        descripcion = input("\tDescripción: ")
        
        respuesta = nota.crear(self.usuario_id, titulo, descripcion)
        if respuesta:
            print(f"\t\tSe creo la nota: {titulo} exitosamente")
        else:
            print(f"No fue posible crear la nota en este momento, vuelve a intentar...")
        funciones.esperarTecla()
    
    def _mostrar_notas(self):
        funciones.borrarPantalla()
        lista_notas = nota.mostrar(self.usuario_id)
        if lista_notas:
            print(f"\n\tMostrar notas")
            print(f"{'ID':<10}{'titulo':<15}{'descripcion':<15}{'fecha':<15}")
            print(f"-" * 80)
            for fila in lista_notas:
                print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
            print(f"-" * 80)
        else:
            print("\n\t No existen notas de acuerdo al usuario")
        funciones.esperarTecla()
    
    def _cambiar_nota(self):
        funciones.borrarPantalla()
        print(f"\n \t .:: {self.nombre} {self.apellidos}, vamos a modificar un Nota ::. \n")
        self._mostrar_notas_lista()
        
        id_nota = input("\t \t ID de la nota a actualizar: ")
        titulo = input("\t Nuevo título: ")
        descripcion = input("\t Nueva descripción: ")
        
        respuesta = nota.cambiar(id_nota, titulo, descripcion)
        if respuesta:
            print(f"\n\t\t Se actualizo la nota: {titulo} exitosamente")
        else:
            print(f"\n\t\t no fue posible actualizar la nota en este momento...")
        funciones.esperarTecla()
    
    def _eliminar_nota(self):
        funciones.borrarPantalla()
        print(f"\n \t .:: {self.nombre} {self.apellidos}, vamos a borrar un Nota ::. \n")
        self._mostrar_notas_lista()
        
        id_nota = input("\t \t ID de la nota a eliminar: ")
        respuesta = nota.borrar(id_nota)
        if respuesta:
            print(f"\n\t\tSe borró la nota exitosamente")
        else:
            print("\n\t\t No fue posible borrar la nota")
        funciones.esperarTecla()
    
    def _mostrar_notas_lista(self):
        notas_lista = nota.mostrar(self.usuario_id)
        if notas_lista:
            print(f"\n\tMostrar notas")
            print(f"{'ID':<10}{'titulo':<15}{'descripcion':<15}{'fecha':<15}")
            print(f"-" * 80)
            for fila in notas_lista:
                print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
            print(f"-" * 80)
        else:
            print("\n\t No existen notas de acuerdo al usuario")
    
    def _opcion_invalida_notas(self):
        print("\n \t \t Opción no válida. Intenta de nuevo.")
        funciones.esperarTecla()


if __name__ == "__main__":
    sistema = SistemaNotas()
    sistema.ejecutar()