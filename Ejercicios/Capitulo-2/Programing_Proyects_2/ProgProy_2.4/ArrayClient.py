import Array

# Crear un arreglo con varios elementos, incluyendo duplicados
maxSize = 10
arr = Array.Array(maxSize)
arr.insert(77)
arr.insert("bar")
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(55)
arr.insert(77)
arr.insert(99)
arr.insert("baz")
arr.insert("bar")

print("Array original con posibles duplicados:")
arr.traverse()

# Llamar al método removeDupes()
arr.removeDupes()
print("\nArray después de eliminar duplicados:")
arr.traverse()

# Crear un arreglo sin duplicados y probar removeDupes()
arr2 = Array.Array(maxSize)
arr2.insert(1)
arr2.insert(2)
arr2.insert(3)
arr2.insert("apple")
arr2.insert("banana")

print("\nArray sin duplicados antes de llamar a removeDupes:")
arr2.traverse()

arr2.removeDupes()
print("\nArray sin duplicados después de llamar a removeDupes (debería ser igual):")
arr2.traverse()
