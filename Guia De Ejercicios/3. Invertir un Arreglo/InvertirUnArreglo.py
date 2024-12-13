# Ejercicio 3.
# Crea una función que reciba un arreglo y devuelva un nuevo arreglo con los elementos en orden inverso.

def invertir_arreglo(arreglo):
    arreglo_invertido = []
    for i in range(len(arreglo) - 1, -1, -1):
        arreglo_invertido.append(arreglo[i])
    return arreglo_invertido

numeros = [1, 2, 3, 4, 5]
resultado = invertir_arreglo(numeros)

print(f"Arreglo original: {numeros}")
print(f"Arreglo invertido: {resultado}")
