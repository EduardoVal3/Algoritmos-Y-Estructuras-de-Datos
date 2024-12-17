# 18
class ListaEnlazada:

    def eliminar_duplicados(self):
        if not self.cabeza:
            return
        valores = set()
        actual = self.cabeza
        previo = None
        while actual:
            if actual.valor in valores:
                previo.siguiente = actual.siguiente
            else:
                valores.add(actual.valor)
                previo = actual
            actual = actual.siguiente
