import  mysql.connector

try:
#conexion con la BD de MySQL
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )

    #Crear un objeto nuevo de tipo cursor para ejecutar SQL
    miCursor = conexion.cursor()

    sql="create database db_python"

    miCursor.execute(sql)

except Exception as e:
    print(f":: Error: {e}")
    print(f":: Tipo de error: {type(e).__name__}")
    print(":: Ocurrio un error por favor vuelva a intentar")
else:
    print("Se creo exitosamente la base de datos")
    miCursor.execute("show databases")
    for x in miCursor:
        print(x)