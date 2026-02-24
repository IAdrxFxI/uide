import random

print("=== GENERADOR DE CONTRASEÑAS ===")

#Pedimos la longitud
longitud = int(input("Ingrese la longitud de la contraseña: "))

#Definimos los caracteres básicos
minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%&*"

#Variable donde guardaremos todos los caracteres posibles
caracteres = ""

#Siempre agregamos minúsculas
caracteres = caracteres + minusculas

#Preguntamos opciones al usuario
usar_mayus = input("¿Desea incluir mayúsculas? (si/no): ")
if usar_mayus == "si":
    caracteres = caracteres + mayusculas

usar_numeros = input("¿Desea incluir números? (si/no): ")
if usar_numeros == "si":
    caracteres = caracteres + numeros
    
usar_simbolos = input("¿Desea incluir símbolos? (si/no): ")
if usar_simbolos == "si":
    caracteres = caracteres + simbolos

# Generamos la contraseña usando una estructura repetitiva
contraseña = ""

for i in range(longitud):
    letra = random.choice(caracteres)
    contraseña = contraseña + letra

# Mostramos el resultado
print("La contraseña generada es:", contraseña)


