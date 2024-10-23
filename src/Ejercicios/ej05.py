'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
 y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
'''

## Preguntamos por el dinero que se ha invertido

def preguntaInvertido():
    cantidadInvertida = int(input("Introduce la cantidad invertida: "))
    return cantidadInvertida

## Preguntamos por el interes anual

def preguntaInteres():
    cantidadInteres = int(input("Introduce el interes anual: "))
    return cantidadInteres

## Preguntamos por los años

def preguntaAnios():
    cantidadAnios = int(input("Introduce el número de años: "))
    return cantidadAnios

## Con esta función se calcula la cantidad final

def cantidadFinal(cantidadInvertida, cantidadInteres, cantidadAnios):
    capital = cantidadInvertida
    for anio in range(1, cantidadAnios + 1):
        capital = capital * (1 + cantidadInteres / 100)
        print(f"Capital al final del año {anio}: {capital:.2f} €")

def main():
    invertido = preguntaInvertido()
    interes = preguntaInteres()
    anios = preguntaAnios()
    
    print(f"\nEl capital obtenido cada año es:")
    cantidadFinal(invertido, interes, anios)

if __name__ == "__main__":
    main()