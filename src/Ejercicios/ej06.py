'''
Escribir un programa que pida al usuario un número entero y 
muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
'''

## Preguntamos por el número de caracteres

def preguntaNumeros():
    cantidad = int(input("Introduce la cantidad invertida: "))
    while cantidad <= 0:
        print("Este número no esta permitido")
        cantidad = int(input("Introduce un número mayor que 0: "))
    return cantidad

def hacerPiramide(cantidad):
    for numero in range(1, cantidad + 1):
        print("*" * numero)
    

def main():
  cantidad1 = preguntaNumeros()
  hacerPiramide(cantidad1)

if __name__ == "__main__":
    main()