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

#EN PROCESO..........................................



