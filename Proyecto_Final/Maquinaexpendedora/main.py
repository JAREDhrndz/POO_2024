from Maquina__ExpendedoramjF import *
from ConexionBD import *

def main():
    db_connection = conexionBD()
    if db_connection is None:
        print("No se pudo conectar a la base de datos.")
        return

    maquina = MaquinaExpendedora("Vending machine", db_connection)

    
    # sabritas = Snacks("B1", "Sabritas", 25, 10)
    # churrumais = Snacks("B2", "Churrumais", 15, 10)
    # gomitas = Golosinas("C1", "Gomitas", 25, 10)
    # chocoretas = Golosinas("C3", "Chocoretas", 20, 10)
    #coca_cola = Bebidas("A1", "Coca Cola", 25, 10)
    # fanta = Bebidas("A3", "Fanta", 20, 10)

    # maquina.agregar_producto(sabritas)
    # maquina.agregar_producto(churrumais)
    # maquina.agregar_producto(gomitas)
    # maquina.agregar_producto(chocoretas)
    #maquina.agregar_producto(coca_cola)
    # maquina.agregar_producto(fanta)

    print("Bienvenido al sistema de la máquina expendedora.")

    while True:
        matricula = input("Por favor, ingrese su matrícula: ").strip().upper()
        if not maquina.buscar_estudiante(matricula):
            print("No está registrado en el sistema. Intente nuevamente.")
            continue
        
      
        nombre = "Nombre_placeholder"  
        carrera = "Carrera_placeholder"  
        usuario = Usuario(matricula, nombre, carrera)

        while True:
            maquina.mostrar_productos()
            codigo_producto = input("Introduce el código del producto que deseas comprar (o 'fin' para salir, '2024' para ver ventas): ").strip().upper()

            if codigo_producto == '2024':
                borrarPantalla()
                maquina.mostrar_ventas(db_connection)
                esperarTecla()
                borrarPantalla()
                continue 
                
            if codigo_producto == 'FIN':
                borrarPantalla()
                print("Gracias por usar el sistema.")
                break

            producto = maquina.seleccionar_producto(codigo_producto)
            if producto:
                print(f"Producto seleccionado: {producto.nombre}")
                print(f"Precio: ${producto.precio}")
            else:
                print("Producto no encontrado o sin stock.")
                continue
            producto_entregado, cambio = usuario.interactuar_maquina(maquina, codigo_producto)

            if producto_entregado:
                print(f"Producto entregado: {producto_entregado.nombre}")
                print(f"Cambio devuelto: ${cambio}")
            else:
                print("No se pudo completar la transacción.")
                if cambio > 0:
                    print(f"Se devolvió el dinero insertado: ${cambio}")
                else:
                    print("No se insertó suficiente dinero.")
        esperarTecla()
        borrarPantalla()
        print("Volver a ingresar matrícula para nueva sesión.")

if __name__ == "__main__":
    main()
