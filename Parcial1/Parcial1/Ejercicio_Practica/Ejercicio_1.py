#permita calcular e imprimir el precio a pagar por un articulo.
#en el precio a pagare se incluye el iva, el programa debera de funcinar n veces
#como el usuario desee

n=int(input("cuantas veces quieres repetir el proceso? "))

print(".::productos::.")
print("coca cola .......$20\nsabritas.....$22\nGomitas......$15")

cf=0
ca=0
for i in range (0,n):

    p=input("Productos deseado:")

    if p=="coca cola":
        c=20
        print(f"${c}")
        
    elif p=="sabritas":
        c=22
        print(f"${c}")
        
    elif p=="gomitas":
        c=15
        print(f"${c}")
        
    else:
        print("NO es un producto que pueda comprar")
    cf=cf+c
    v=cf*0.16
    ca=cf+v

print(f"el iva es: {v}")
print(f"El costo de los productos que compraste es ${ca}")