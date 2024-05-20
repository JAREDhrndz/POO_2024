num1 = input("Por favor, introduce el primer número entero: ")
num2 = input("Por favor, introduce el segundo número entero: ")
n1_e = int(num1)
n2_e = int(num2)

print(f"Los numeros entre el numero {n1_e} y el numero {n2_e} son:")
i=1
for i in range (n1_e+1,n2_e):
    print(i)