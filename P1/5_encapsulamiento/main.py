from coches import *

#Solicitar los datos que posteriormente seran los atributos del objeto

numm_coches=int(input("Cuantos vehiculos desea ingresar: "))

for i in range(0, numm_coches):
    print(f"\n\t . . . Datos del Vehiculo #{i+1} . . . ")
    marca=input("Ingresar la marca: ").upper()
    color=input("Ingresar el color: ").upper()
    modelo=input("Ingresar el modelo: ").upper()
    velocidad=int(input("Ingresar la velocidad: "))
    caballaje=int(input("Ingresar el caballaje: "))
    plazas=int(input("Ingresar el numero de plazas: "))

    coche1=Coches(marca, color, modelo, velocidad, caballaje, plazas)


    print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}")

    esperarTecla()
# coche1=Coches("VW", "Blanco", "2022", 220, 150, 5)
# coche2=Coches("Nissan", "Azul", "2020", 180, 150, 6)
# coche3=Coches("Honda", "", "", 0, 0, 0)
# coche4=Coches("", "", "", 0, 0, 0)
# coche4.marca2="Mazda"
# print(coche4.marca2)

# coche1.num_serie="1234ABC"



# print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} \n Numero de serie:{coche1.num_serie}")

# print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

# print(coche3.marca)