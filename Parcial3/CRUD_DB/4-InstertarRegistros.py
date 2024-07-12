from ConexionDB import *

try:
    miCursor = conexion.cursor()
    sql = "INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL', 'Jared Alonso', 'Col. Niños Heroes #108', '6181552254')"
    miCursor.execute(sql)
    conexion.commit()
    #Es necesario ejecutar el comit para que finalice el insert
except:
    print(":> Ocurrio un error por favor vuelva a intentar")
else:
    print("Se creo la tabla exitosamente")
