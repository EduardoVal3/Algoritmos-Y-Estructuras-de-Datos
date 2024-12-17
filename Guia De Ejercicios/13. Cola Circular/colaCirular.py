# 13
class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = -1
        self.final = -1

    def esta_llena(self):
        return (self.final + 1) % self.capacidad == self.frente

    def esta_vacia(self):
        return self.frente == -1

    def enqueue(self, dato):
        if self.esta_llena():
            print("Cola llena")
            return
        if self.esta_vacia():
            self.frente = 0
        self.final = (self.final + 1) % self.capacidad
        self.cola[self.final] = dato

    def dequeue(self):
        if self.esta_vacia():
            print("Cola vacía")
            return None
        dato = self.cola[self.frente]
        if self.frente == self.final:
            self.frente = self.final = -1
        else:
            self.frente = (self.frente + 1) % self.capacidad
        return dato

# Ejemplo de uso
cola = ColaCircular(5)
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
print(cola.dequeue())  # 10
cola.enqueue(40)
