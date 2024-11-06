from Deque import Deque

deque = Deque(5)  # Crear una deque con tamaño máximo de 5 elementos

# Insertar elementos en ambos extremos
deque.insertLeft(1)
deque.insertRight(2)
deque.insertLeft(3)
deque.insertRight(4)
deque.insertLeft(5)

print("Contenido del deque después de las inserciones:", deque)

# Intentar insertar en una deque llena
try:
    deque.insertRight(6)
except Exception as e:
    print(e)

# Eliminar elementos de ambos extremos
print("Elemento eliminado desde la izquierda:", deque.removeLeft())
print("Elemento eliminado desde la derecha:", deque.removeRight())

# Ver contenido actual del deque
print("Contenido del deque después de las eliminaciones:", deque)

# Mostrar los elementos en ambos extremos
print("Elemento en el extremo izquierdo:", deque.peekLeft())
print("Elemento en el extremo derecho:", deque.peekRight())

# Comprobar si la deque está vacía o llena
print("¿Está la deque vacía?", deque.isEmpty())
print("¿Está la deque llena?", deque.isFull())
