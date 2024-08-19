from ConexionBD import *

class Moneda:
    def __init__(self, valor):
        self.valor = valor
    
    def getValor(self):
        return self.valor

class Monedero:
    def __init__(self):
        self.monedas = 0
        self.monedas_aceptadas = [5, 10]

    def agregar_monedas(self, moneda):
        if moneda.valor in self.monedas_aceptadas:
            self.monedas += moneda.valor

    def devolver_cambio(self):
        cambio = self.monedas
        self.monedas = 0
        return cambio

    def verifica_monedas(self, moneda):
        return moneda.valor in self.monedas_aceptadas

class Producto:
    def __init__(self, codigo, nombre, precio, stock, tipo_producto):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.tipo_producto = tipo_producto

    @staticmethod
    def obtener_productos(db_connection):
        query = "SELECT codigo, nombre, precio, stock, tipo_producto FROM productos"
        rows = fetch_all(db_connection, query)
        productos = []
        for row in rows:
            producto = Producto(row[0], row[1], row[2], row[3], row[4])
            productos.append(producto)
        return productos

    def actualizar_precio(self, precio, db_connection):
        self.precio = precio
        query = "UPDATE productos SET precio = %s WHERE codigo = %s"
        ejecutar_query(db_connection, query, (precio, self.codigo))

    def actualizar_stock(self, db_connection):
    
        query = "UPDATE productos SET stock = stock - 1 WHERE codigo = %s AND stock > 0"
        ejecutar_query(db_connection, query, (self.codigo,))
        self.stock -= 1
    def disponible(self):
        return self.stock > 0

class Snacks(Producto):
    def __init__(self, codigo, nombre, precio, stock):
        super().__init__(codigo, nombre, precio, stock, "Snacks")

class Golosinas(Producto):
    def __init__(self, codigo, nombre, precio, stock):
        super().__init__(codigo, nombre, precio, stock, "Golosinas")

class Bebidas(Producto):
    def __init__(self, codigo, nombre, precio, stock):
        super().__init__(codigo, nombre, precio, stock, "Bebidas")

class Transaccion:
    def __init__(self):
        self.producto = None
        self.costo_insertado = 0

    def iniciar_transaccion(self, producto, costo):
        self.producto = producto
        self.costo_insertado = costo

    def completar_transaccion(self):
        if self.costo_insertado >= self.producto.precio:
            self.producto.stock -= 1
            return True
        return False

    def cancelar_transaccion(self):
        self.producto = None
        self.costo_insertado = 0

class MaquinaExpendedora:
    def __init__(self, nombre, db_connection):
        self.nombre = nombre
        self.db_connection = db_connection
        self.lista_productos = Producto.obtener_productos(db_connection)
        self.monedero = Monedero()

    def agregar_producto(self, producto):
        query = """
        INSERT INTO productos (codigo, nombre, precio, stock, tipo_producto)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE nombre = VALUES(nombre), precio = VALUES(precio), stock = VALUES(stock), tipo_producto = VALUES(tipo_producto)
        """
        ejecutar_query(self.db_connection, query, (producto.codigo, producto.nombre, producto.precio, producto.stock, producto.tipo_producto))
        self.lista_productos = Producto.obtener_productos(self.db_connection)

    def seleccionar_producto(self, codigo):
        for producto in self.lista_productos:
            if producto.codigo == codigo:
                return producto
        return None

    def ingresar_moneda(self, moneda):
        self.monedero.agregar_monedas(moneda)

    def entregar_producto(self, producto, matricula):
        if producto.disponible():
            producto.actualizar_stock(self.db_connection)
            self.guardar_venta(producto.codigo, matricula)
            return producto
        else:
            print("Producto fuera de stock.")
            return None

    def mostrar_costo(self, producto):
        return producto.precio

    def devolver_cambio(self):
        return self.monedero.devolver_cambio()

    def mostrar_productos(self):
        for producto in self.lista_productos:
            print(f"{producto.nombre}\n Codigo: {producto.codigo}\n Precio: ${producto.precio}\n Stock: {producto.stock}")

    def mostrar_ventas(self, connection):
        query = "SELECT * FROM ventas"
        ventas = fetch_all(connection, query)
        
        print("Ventas realizadas en consola:")
        for venta in ventas:
            id_venta = venta[0]  
            fecha = venta[1]
            hora = venta[2]
            matricula = venta[3]
            codigo = venta[4]
            print(f"ID: {id_venta}, Fecha: {fecha}, Hora: {hora}, Matrícula: {matricula}, Código: {codigo}")

    def buscar_estudiante(self, matricula):
        query = "SELECT * FROM estudiantes WHERE matricula = %s"
        result = fetch_one(self.db_connection, query, (matricula,))
        return result is not None

    def guardar_venta(self, codigo, matricula):
        query = """
        INSERT INTO ventas (fecha, hora, matricula, codigo)
        VALUES (CURDATE(), CURTIME(), %s, %s)
        """
        params = (matricula, codigo)
        try:
            ejecutar_query(self.db_connection, query, params)
        except Exception as e:
            print(f"Error en la consulta: {e}")


class Usuario:
    def __init__(self, matricula, nombre, carrera):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera

    def interactuar_maquina(self, maquina, codigo_producto):
        producto = maquina.seleccionar_producto(codigo_producto)
        
        if not producto:
            print("Producto no encontrado.")
            return None, 0
        if not producto.disponible():
            print("Producto no disponible.")
            return None, 0

        total_insertado = 0
        while total_insertado < producto.precio:
            valor_moneda = int(input("Introduce el valor de la moneda (5 o 10): "))
            moneda = Moneda(valor_moneda)
            if not maquina.monedero.verifica_monedas(moneda):
                print("Moneda no aceptada.")
                continue
            maquina.ingresar_moneda(moneda)
            total_insertado += moneda.valor
            print(f"Total insertado: ${total_insertado}")
        producto_entregado = maquina.entregar_producto(producto, self.matricula)
        
        cambio = total_insertado - producto.precio
        maquina.monedero.devolver_cambio()  
        return producto_entregado, cambio
