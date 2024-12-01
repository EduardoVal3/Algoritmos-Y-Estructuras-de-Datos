# Código para probar la implementación
from BinarySearchTreeProgProy import BinarySearchTree

# Crear un árbol binario de búsqueda
tree = BinarySearchTree()

# Insertar claves con duplicados
tree.insert(65, "A")
tree.insert(65, "B")
tree.insert(65, "C")
tree.insert(44, "D")
tree.insert(44, "E")
tree.insert(81, "F")

# Imprimir el árbol en orden
print("Árbol en orden (in-order):")
print(tree.traverse("in"))

# Buscar la clave duplicada más profunda y la más superficial
print("Buscar clave 65 (más profunda):", tree.search(65, find_deepest=True))
print("Buscar clave 65 (más superficial):", tree.search(65, find_deepest=False))

# Eliminar duplicados en orden LIFO
print("\nEliminando claves duplicadas de 65:")
print("Eliminar 65 (LIFO):", tree.delete(65))
print("Árbol después de eliminar 65:")
print(tree.traverse("in"))

print("Eliminar 65 (LIFO):", tree.delete(65))
print("Árbol después de eliminar 65:")
print(tree.traverse("in"))

print("Eliminar 65 (LIFO):", tree.delete(65))
print("Árbol después de eliminar 65:")
print(tree.traverse("in"))

