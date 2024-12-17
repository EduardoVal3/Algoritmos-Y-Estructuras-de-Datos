# 17
class ListaEnlazada:
    # Métodos anteriores...

    def invertir(self):
        previo = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = previo
            previo = actual
            actual = siguiente
        self.cabeza = previo
