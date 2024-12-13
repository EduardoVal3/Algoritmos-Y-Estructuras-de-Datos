# Ejercicio 5.
# Crea una función que elimine los valores duplicados de un arreglo y devuelva un nuevo arreglo con valores únicos.

def eliminar_duplicados(arreglo):
    return list(dict.fromkeys(arreglo))

numeros = [1, 2, 2, 3, 4, 4, 5]
print(eliminar_duplicados(numeros)) 
