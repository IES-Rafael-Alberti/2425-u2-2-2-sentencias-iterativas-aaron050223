'''Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.'''

def tablas():
    for numero1 in range(1, 11):  
        print(f"Tabla del número {numero1}:")
        for numero2 in range(1, 11):  
            print(f"{numero1} x {numero2} = {numero1 * numero2}")
        print()

def main():
    tablas()

if __name__ == "__main__":
    main()