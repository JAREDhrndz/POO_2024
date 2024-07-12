from ConexionDB import *

try:
    miCursor = conexion.cursor()
    sql = "update from clientes set direccion='Col. Nueva' where id=1"
    miCursor.execute(sql)
    conexion.commit()
    #Es necesario ejecutar el comit para que finalice el insert
except:
    print(":: Ocurrio un error por favor vuelva a intentar")
else:
    print("Se borró el registro exitosamente")