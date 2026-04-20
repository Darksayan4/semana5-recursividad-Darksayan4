"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""
n=int(input("Ingrese un numero positivo: "))

def factorial_ciclo(n):
    res=1
    for i in range (1,n+1)
        res *= i
    return res 

def factorial_recursivo(n):
    if n==0||n==1
        return 1
    return n * factorial_recursivo(n-1)

print("El factorial con ciclo es: ",factorial_ciclo(n))
print("El factorial con recursividad es: ",factorial_recursivo(n))
