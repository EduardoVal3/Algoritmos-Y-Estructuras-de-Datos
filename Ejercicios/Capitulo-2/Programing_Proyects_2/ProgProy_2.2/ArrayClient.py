import Array

maxSize = 10  # Tamaño máximo del arreglo
arr = Array.Array(maxSize)  # Crea un objeto de tipo Array

# Inserta varios elementos de distintos tipos
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

print("Array inicial con", len(arr), "elementos:")
arr.traverse()

# Prueba el método deleteMaxNum()
max_num = arr.deleteMaxNum()
print("\nEl valor numérico máximo eliminado del arreglo es:", max_num)
print("Array después de eliminar el número máximo:")
arr.traverse()

# Prueba con un arreglo que no contiene números
arr2 = Array.Array(maxSize)
arr2.insert("apple")
arr2.insert("banana")
arr2.insert("cherry")
print("\nArray que solo contiene cadenas:")
arr2.traverse()
max_num = arr2.deleteMaxNum()
print("El valor numérico máximo eliminado en este arreglo es:", max_num)
print("Array después de intentar eliminar el número máximo (sin números):")
arr2.traverse()
