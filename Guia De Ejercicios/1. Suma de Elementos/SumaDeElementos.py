# Ejercicio 1.
# Escribir un programa que tome un arreglo de números y calcule la suma de todos los elementos.

def suma_arreglo(arreglo):
    suma_total = 0
    for numero in arreglo:
        suma_total += numero
    return suma_total

numeros = [8, 6, 6, 5, 5]
resultado = suma_arreglo(numeros)

print(f"La suma total es: {resultado}")
