#concatenar cadenas de caracteres con contenido de variables 

nombre="Eduardo";
especialidad="Area de Desarrollo de SW Multiplataforma";
Carrera="Ingeniero en Gestion y Desarrollo de SW";

#ra forma de concatenar

print("MI nombre es:"+nombre ,",estoy en la especialidad de "+especialidad , "en la carrera de "+Carrera)

print("\n");
#2da forma 

print("MI nombre es:",nombre ,",estoy en la especialidad de ",especialidad , "en la carrera de ",Carrera)

print("\n");
#3ra forma 

print(f"MI nombre es:{nombre} estoy en la especialidad de:{especialidad} en la carrera de: {Carrera}")

print("\n");
#4ta forma 
print("Mi nombre es:{} Estoy rn la especialidad de: {} en la carrera de: {}" .format(nombre,especialidad,Carrera))

print("\n");

#5ta forma 
print('Mi nombre es: '+nombre+' estoy en la especialidad de: '+especialidad+', en la carrera de: '+Carrera)

print("\n");
