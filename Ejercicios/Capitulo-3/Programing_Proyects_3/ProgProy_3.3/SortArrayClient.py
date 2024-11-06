from SortArray import *
import random
import timeit

def initArray(size=100, maxValue=100, seed=3.14159):
    """Crea un Array con una secuencia 'aleatoria' de elementos."""
    arr = Array(size)  # Crear un objeto Array
    random.seed(seed)  # Establecer la semilla para el generador de números aleatorios
    for i in range(size):  # Insertar elementos aleatorios en el arreglo
        arr.insert(random.randrange(maxValue))
    return arr  # Retorna el Array creado

# Inicializar un arreglo con 100 elementos y valores aleatorios
arr = initArray(size=20, maxValue=10)
print("Arreglo original:")
print(arr)

# Ordenar el arreglo usando un algoritmo de ordenación (puedes usar bubbleSort, selectionSort, etc.)
arr.bubbleSort()  # Usamos bubbleSort para ordenar el arreglo
print("\nArreglo ordenado:")
print(arr)

# Añadir duplicados manualmente para probar la deduplicación
arr.insert(5)  # Insertar un duplicado del valor 5
arr.insert(3)  # Insertar un duplicado del valor 3
arr.insert(3)  # Insertar otro duplicado del valor 3
print("\nArreglo con duplicados:")
print(arr)

# Aplicar el método deduplicate para eliminar los duplicados
arr.deduplicate()
print("\nArreglo después de eliminar duplicados:")
print(arr)

# Comprobamos que el tamaño ha cambiado (si hay duplicados)
print("\nNúmero de elementos después de eliminar duplicados:", len(arr))