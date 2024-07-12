import  mysql.connector

try:
#conexion con la BD de MySQL
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_python'
    )
except Exception as e:
    print("::: Ocurrio un error por favor vuelva a intentar")
