from ConexionDB import *

try:
    miCursor = conexion.cursor()
    sql = "select * from clientes"

    miCursor.execute(sql)
    resultado = miCursor.fetchall()

    for fila in resultado:
            print(f"id:{fila(0)} - Nombre: {fila(1)} - Dirección:{fila(2)} - Telefono: {fila(3)}")

except:
    print(":: Ocurrio un error por favor vuelva a intentar")
else:
    print("Se creo la tabla exitosamente")
