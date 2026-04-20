"""
Ejercicio 5:
Calcular la potencia de una base elevada a un exponente entero positivo.
"""
base=int(input("Ingrese un numero base de la potencia: "))
exponente=int(input("Ingrese el numero por el cual va a elevar: "))

def potencia_ciclo(base, exponente):
    resultado =1
    for i in range (exponente):
        resultado *= base
    return resultado

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia_recursiva(base,exponente-1)

print("La potencia usando ciclo es: ",potencia_ciclo(base,exponente))
print("La potencia usando recursividad: ",potencia_recursividad(base,exponente))
