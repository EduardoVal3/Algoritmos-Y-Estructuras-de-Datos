# Ejercicio 11.
# Crea una clase Cola que implemente las operaciones básicas: enqueue, dequeue y peek.

class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else None

    def peek(self):
        return self.items[0] if self.items else None

# Ejemplo
cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
print(cola.dequeue())  # 1
