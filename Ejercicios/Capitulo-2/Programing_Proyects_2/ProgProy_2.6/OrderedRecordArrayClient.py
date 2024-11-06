from OrderedRecordArray import OrderedRecordArray

def second(x):  # Función clave en el segundo elemento del registro
    return x[1]

# Tamaño máximo del arreglo
maxSize = 20
arr = OrderedRecordArray(maxSize, key=second)  # Crea un objeto OrderedRecordArray

# Inserta elementos en el array, incluyendo algunos duplicados
records_to_insert = [
    ('a', 5), ('b', 3), ('c', 7), ('d', 3),
    ('e', 5), ('f', 9), ('g', 5), ('h', 3),
    ('i', 7), ('j', 3), ('k', 1), ('l', 9)
]

for record in records_to_insert:
    arr.insert(record)

# Muestra el contenido del array después de insertar los elementos
print("Contenido del arreglo después de las inserciones:")
arr.traverse()

# Prueba de eliminación de elementos con claves duplicadas
print("\nPruebas de eliminación:")
records_to_delete = [('a', 5), ('d', 3), ('f', 9), ('x', 4)]  # Incluye un elemento inexistente para probar

for record in records_to_delete:
    result = arr.delete(record)
    print(f"Eliminando {record}: {'Éxito' if result else 'Fallido (no encontrado)'}")

# Muestra el contenido del array después de eliminar los elementos
print("\nContenido del arreglo después de las eliminaciones:")
arr.traverse()
