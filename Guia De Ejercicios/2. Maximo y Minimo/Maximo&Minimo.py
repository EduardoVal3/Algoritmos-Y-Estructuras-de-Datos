# Ejercicio 2.
# Dado un arreglo de números, encuentra el valor máximo y el mínimo sin usar funciones predefinidas como max o min.

def encontrar_max_min(arreglo):
    if not arreglo:  
        return None, None

    maximo = minimo = arreglo[0]  

    for numero in arreglo:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

    return maximo, minimo

numeros = [3, 1, 4, 1, 5, 9, -2, 6]
maximo, minimo = encontrar_max_min(numeros)

print(f"El máximo es: {maximo}")
print(f"El mínimo es: {minimo}")
