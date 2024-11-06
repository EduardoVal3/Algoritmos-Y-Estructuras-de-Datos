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

print("Array con", len(arr), "elementos:")
arr.traverse()

# Prueba el método getMaxNum()
max_num = arr.getMaxNum()
print("El valor numérico máximo en el arreglo es:", max_num)

# Prueba con un arreglo que no contiene números
arr2 = Array.Array(maxSize)
arr2.insert("apple")
arr2.insert("banana")
arr2.insert("cherry")
print("\nArray que solo contiene cadenas:")
arr2.traverse()
print("El valor numérico máximo en este arreglo es:", arr2.getMaxNum())
