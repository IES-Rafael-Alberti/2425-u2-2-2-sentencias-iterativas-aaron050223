'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''

contraseña = "MbappeVinicius"

intento = input("Introduce la contraseña: ")

while contraseña != intento:
    intento = input("Contraseña incorrecta, intentalo de nuevo: ")

print("Contraseña correcta.")