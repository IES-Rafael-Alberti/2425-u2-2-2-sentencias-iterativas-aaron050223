'''
Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''

## Le pedimos el número entero al usuario y que se positivo

def pedirNum():
    numero = int(input("Introduce un número entero y positivo: "))
    if numero <=0:
        print("El numero no cumple los parametros")
        return pedirNum()
    return numero

## Ahora hacemos una funcion para quedarnos con los números impares

def paraImpares(numero):
    impares = []
    for a in range(1,numero +1):
        if a % 2 != 0: ## con este modulo confirmamos si es o no impar
            impares.append(a) ## el .append lo uso para añadir a 'a' todos los numeros que consigan pasar el if(osea los impares).
    return impares

def main():

    numero = pedirNum()
    impares = paraImpares(numero)

    print(f"Los números impares son: {', '.join(map(str, impares))}") ## el '.join' une los elementos con el caracter que se le indique (una coma en este caso)

if __name__ == "__main__":
    main()