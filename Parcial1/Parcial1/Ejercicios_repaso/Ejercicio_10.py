i=1 
calf=0 
reprobado=0
aprobado=0
cantA=0
cantR=0

for i in range(1,16):

    calf=int(input(f"Ingrese la calificación del alumno {i}: "))

    #contador de aprobados y reprobados
    if calf>=60:
        aprobado=aprobado+1
    else:
        reprobado=reprobado+1

print(f"La cantidad de aprobados es: {aprobado}")
print(f"La cantidad de reprobados es: {reprobado}")