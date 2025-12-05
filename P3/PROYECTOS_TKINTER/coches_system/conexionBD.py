<<<<<<< HEAD:P3/proyectos_tkinter/coches_system/conexionBD.py
import mysql.connector

try:
    conexion=mysql.connector.connect(
    port="3306",    
    host="127.0.0.1",
    user="root",
    password="",
    database="bd_coches"
    )
    cursor=conexion.cursor(buffered=True)
except:
=======
import mysql.connector

try:
    conexion=mysql.connector.connect(
    port="3306",    
    host="127.0.0.1",
    user="root",
    password="",
    database="bd_coches"
    )
    cursor=conexion.cursor(buffered=True)
except:
>>>>>>> 66bf4bbadb48bf3c558ceda7540154e5a15da746:P3/PROYECTOS_TKINTER/coches_system/conexionBD.py
    print("Ocurrio un error con la base de datos... Verifique")