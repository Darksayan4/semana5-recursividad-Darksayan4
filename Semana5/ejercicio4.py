"""
Ejercicio 4:
Dado un número entero positivo N, contar cuántos números pares existen entre 1 y N.
"""
n=int(input("Ingrese un numero positivo: "))

def contar_pares_ciclo(n):
    contador=0
    for i in range (1,n+1)
        if i % 2 == 0:
            return contador+=1
    return contador

def contar_pares_recursivo(n):
    if n==0:
        return 0
    if n % == 0:
        return 1 + contador_pares_recursivo(n-1)
    return contador_pares_recursivo(n-1)
    
print("Cantidad de pares con ciclo: ",contador_pares_ciclo(n))
print("Cantidad de pares con recursividad: ",contador_pares_recursivo(n))
