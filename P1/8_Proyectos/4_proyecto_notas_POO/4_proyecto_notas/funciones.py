import os

class SistemaUtilidades:
    @staticmethod
    def borrarPantalla():
        os.system("cls")
    
    @staticmethod
    def esperarTecla():
        input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")
    
    @staticmethod
    def menu_usurios():
        print("\n \t.:: Sistema de Gestión de Notas ::..")
        print("\t\t1.- Registro")
        print("\t\t2.- Login")
        print("\t\t3.- Salir")
        opcion = input("\t\t Elige una opción: ").upper().strip()
        return opcion
    
    @staticmethod
    def menu_notas():
        print("\n \t .::  Menu Notas ::.")
        print("\t1.- Crear")
        print("\t2.- Mostrar")
        print("\t3.- Cambiar")
        print("\t4.- Eliminar")
        print("\t5.- Salir")
        opcion = input("\t\t Elige una opción: ").upper().strip()
        return opcion
    
    @staticmethod
    def formatear_texto(texto):
        return texto.strip()

# Funciones estáticas para mantener compatibilidad
def borrarPantalla():
    SistemaUtilidades.borrarPantalla()

def esperarTecla():
    SistemaUtilidades.esperarTecla()

def menu_usurios():
    return SistemaUtilidades.menu_usurios()

def menu_notas():
    return SistemaUtilidades.menu_notas()