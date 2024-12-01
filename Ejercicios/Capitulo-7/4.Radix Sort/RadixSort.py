# Función auxiliar: Counting Sort en base al dígito representado por exp
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Array para almacenar resultados ordenados
    count = [0] * 10  # Array de conteo para los dígitos (0-9)

    # Contar ocurrencias de dígitos en la posición actual (exp)
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    # Convertir el array de conteo a índices acumulados
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el array ordenado
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copiar el resultado en el array original
    for i in range(n):
        arr[i] = output[i]

# Función principal: Radix Sort
def radix_sort(arr):
    # Encontrar el número máximo para determinar el número de dígitos
    max_val = max(arr)
    exp = 1  # Inicializamos el divisor en 1

    # Ordenar por cada posición de dígito
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Datos de entrada: IDs de estudiantes
student_ids = [324, 125, 654, 512, 233, 789, 100]

print("IDs originales:", student_ids)

# Aplicar Radix Sort
radix_sort(student_ids)

print("IDs ordenados:", student_ids)
