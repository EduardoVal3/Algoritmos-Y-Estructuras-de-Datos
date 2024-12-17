# 19
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

def fusionar_listas(lista1, lista2):
    dummy = Nodo(0)
    actual = dummy
    p1, p2 = lista1.cabeza, lista2.cabeza

    while p1 and p2:
        if p1.valor < p2.valor:
            actual.siguiente = p1
            p1 = p1.siguiente
        else:
            actual.siguiente = p2
            p2 = p2.siguiente
        actual = actual.siguiente

    actual.siguiente = p1 or p2  # Agregar el resto de la lista no vacía
    resultado = ListaEnlazada()
    resultado.cabeza = dummy.siguiente
    return resultado

# Ejemplo de uso
lista1 = ListaEnlazada()
lista2 = ListaEnlazada()
for val in [1, 3, 5]:
    lista1.agregar_al_final(val)
for val in [2, 4, 6]:
    lista2.agregar_al_final(val)

resultado = fusionar_listas(lista1, lista2)
resultado.mostrar()  # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
