# Ejercicio 4.
# Escribe un programa que tome un arreglo y un número, y determine si el número está presente en el arreglo.
def buscar_elemento(arreglo, numero):
    return numero in arreglo

numeros = [1, 2, 3, 4, 5]
print(buscar_elemento(numeros, 3))  
print(buscar_elemento(numeros, 6))  
