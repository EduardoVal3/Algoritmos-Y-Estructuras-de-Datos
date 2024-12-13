# Ejercicio 6.
# Crea una clase Pila que implemente las operaciones básicas: push, pop y peek. Prueba la clase añadiendo y quitando elementos.

class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.esta_vacia() else None

    def peek(self):
        return self.items[-1] if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.items) == 0

# Ejemplo
pila = Pila()
pila.push(1)
pila.push(2)
print(pila.peek())  # 2
print(pila.pop())   # 2
print(pila.esta_vacia())  # False
