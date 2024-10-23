'''
Escribir un programa que pida al usuario un número entero positivo y
 muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''

## Le pedimos el número entero al usuario y que se positivo

def pedirNum():
    numero = int(input("Introduce un número entero y positivo: "))
    if numero <0:
        print("El numero no cumple los parametros")
        return pedirNum()
    return numero

## Ahora hacemos una funcion para rir retordeciendo hasta llegar al 0

def cuentaAtras(numero):
    return list(range(numero,-1,-1))

def main():

    numero = pedirNum()
    cuenta = cuentaAtras(numero)

    print(f"Los números impares son: {', '.join(map(str, cuenta))}") ## el '.join' une los elementos con el caracter que se le indique (una coma en este caso)

if __name__ == "__main__":
    main()