'''
Escribir un programa que pregunte al usuario su edad y 
muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''

## Pedimos la edad

edad = int(input("introduzca su edad: "))

## En esta funcion se entregara como la actividad indica

def main():
    for numero in range(1,edad +1):
        print(numero)
if __name__ == "__main__":
    main()