from SortArray import *
import random
import timeit

def initArray(size=100, maxValue=100, seed=3.14159):
    """Crear un arreglo de tamaño especificado con una secuencia
    fija de elementos aleatorios."""
    # Crear el objeto Array con el tamaño dado
    arr = Array(size)
    # Establecer la semilla para el generador de números aleatorios
    random.seed(seed)
    # Insertar números aleatorios en el arreglo
    for i in range(size):
        arr.insert(random.randrange(maxValue))
    return arr  # Devolver el arreglo lleno

# Inicializar el arreglo y mostrar su contenido
arr = initArray()
print("Array containing", len(arr), "items:\n", arr)

# Probar los métodos de ordenamiento y medir el tiempo que toman
for test in ['initArray().bubbleSort()', 'initArray().selectionSort()', 'initArray().insertionSort()']:
    # Ejecuta cada prueba 100 veces y mide el tiempo total
    elapsed = timeit.timeit(test, number=100, globals=globals())
    print(test, "took", elapsed, "seconds", flush=True)

# Ordenar el arreglo y mostrarlo
arr.insertionSort()
print('Sorted array contains:\n', arr)

# Calcular y mostrar la mediana del arreglo
print('Median of the array is:', arr.median())