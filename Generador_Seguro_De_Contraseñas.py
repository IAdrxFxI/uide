import random

print("=== GENERADOR DE CONTRASEÑAS ===")

# Pedimos la longitud con validación simple
while True:
    entrada = input("Ingrese la longitud de la contraseña: ")
    
    if entrada.isdigit():  # Verifica que sea número
        longitud = int(entrada)
        if longitud > 0:
            break
        else:
            print("Ingrese un número mayor que 0.")
    else:
        print("Ingrese un número válido.")

# Definimos los caracteres básicos
minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%&*"

caracteres = ""
caracteres += minusculas  # Siempre agregamos minúsculas

# Preguntamos opciones
usar_mayus = input("¿Desea incluir mayúsculas? (si/no): ").lower()
if usar_mayus == "si":
    caracteres += mayusculas

usar_numeros = input("¿Desea incluir números? (si/no): ").lower()
if usar_numeros == "si":
    caracteres += numeros
    
usar_simbolos = input("¿Desea incluir símbolos? (si/no): ").lower()
if usar_simbolos == "si":
    caracteres += simbolos

# Generamos la contraseña
contraseña = ""

for i in range(longitud):
    letra = random.choice(caracteres)
    contraseña += letra

# Mostramos el resultado
print("La contraseña generada es:", contraseña)



