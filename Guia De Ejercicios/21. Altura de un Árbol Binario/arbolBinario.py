# 21
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda:
                self._insertar(nodo.izquierda, valor)
            else:
                nodo.izquierda = NodoArbol(valor)
        else:
            if nodo.derecha:
                self._insertar(nodo.derecha, valor)
            else:
                nodo.derecha = NodoArbol(valor)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if not nodo:
            return False
        if nodo.valor == valor:
            return True
        if valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        else:
            return self._buscar(nodo.derecha, valor)

    def inorder(self):
        self._inorder(self.raiz)

    def _inorder(self, nodo):
        if nodo:
            self._inorder(nodo.izquierda)
            print(nodo.valor, end=" ")
            self._inorder(nodo.derecha)

# Ejemplo de uso
arbol = ArbolBinario()
for val in [10, 5, 15, 2, 7]:
    arbol.insertar(val)

arbol.inorder()  # 2 5 7 10 15
print(arbol.buscar(7))  # True
print(arbol.buscar(20))  # False
