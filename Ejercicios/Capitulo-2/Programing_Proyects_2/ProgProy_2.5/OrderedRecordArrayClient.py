from OrderedRecordArray import *
def second(x): # Key on second element of record
 return x[1]

# Crear dos arreglos ordenados con la misma función clave
arr1 = OrderedRecordArray(10, second)
arr2 = OrderedRecordArray(10, second)

# Insertar elementos en arr1
for rec in [('a', 1.5), ('b', 2.1), ('c', 4.3)]:
    arr1.insert(rec)

# Insertar elementos en arr2
for rec in [('d', 0.5), ('e', 3.1), ('f', 5.2)]:
    arr2.insert(rec)

print("Arreglo 1 antes de la fusión:")
arr1.traverse()

print("\nArreglo 2 antes de la fusión:")
arr2.traverse()

# Fusionar arr2 en arr1
arr1.merge(arr2)

print("\nArreglo 1 después de la fusión:")
arr1.traverse()
