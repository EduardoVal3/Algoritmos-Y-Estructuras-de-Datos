import Array

# Crear un arreglo con varios elementos de diferentes tipos
maxSize = 10
arr = Array.Array(maxSize)
arr.insert(77)
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)

print("Array original con elementos:")
arr.traverse()

# Crear un nuevo arreglo para almacenar los elementos en orden descendente
sorted_array = Array.Array(maxSize)

# Usar deleteMaxNum() para extraer y almacenar elementos ordenados
while True:
    max_num = arr.deleteMaxNum()  # Obtener y eliminar el valor numérico más alto
    if max_num is None:  # Si no quedan números, termina el ciclo
        break
    sorted_array.insert(max_num)  # Insertar el número más alto en el arreglo ordenado

# Mostrar el arreglo ordenado en orden descendente
print("\nArreglo ordenado en orden descendente:")
sorted_array.traverse()
