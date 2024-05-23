resp="SI"
numP=0
while resp=="SI":
    nom = input("Nombre del paciente: ")
    tipoS = input("Tipo de sangre: ")

    #SISTOLICA
    si1 = int(input("Primera medición SIStolica: "))
    si2 = int(input("Segunda medición SIStolica: "))
    si3 = int(input("Tercera medición SIStolica: "))

    #DIASTOLICA
    dia1 = int(input("Primera medición DIAstolica: "))
    dia2 = int(input("Segunda medición DIAstolica: "))
    dia3 = int(input("Tercera medición DIAstolica: "))

    #FINAL
    fin = int(input("Medición final del dia: "))

    #CALCULAR
    parcialSI=(si1+si2+si3)/3
    parcialDIA=(dia1+dia2+dia3)/3
    final=(parcialSI+parcialDIA+fin)/3
    
    #IMPRIMIR
    input(f"El primedio parcial de presión SIStolica es {parcialSI}")
    input(f"El primedio parcial de presión DIAstolica es {parcialDIA}")
    input(f"La presión final total es {final}")

    #CONDICIONAL
    if parcialSI<=120 or parcialDIA<=80:
        print("Tiene una presión normal")
    else:
        print("Tiene una presion anormal")

    #ACUMULADOR
    numP=numP+1

    #PREGUNTA
    resp = input("Desea ingresar otro paciente? ")
    

print(f"Los pacientes capturados fueron: {numP}")
