# 22
import arbolBinario
from collections import deque

def recorrido_por_niveles(raiz):
    if not raiz:
        print("El árbol está vacío")
        return
    cola = deque([raiz])
    while cola:
        nodo = cola.popleft()
        print(nodo.valor, end=" ")
        if nodo.izquierda:
            cola.append(nodo.izquierda)
        if nodo.derecha:
            cola.append(nodo.derecha)
    print()  # Salto de línea al final

# Ejemplo de uso
arbol = arbolBinario()
for val in [10, 5, 15, 2, 7]:
    arbol.insertar(val)

recorrido_por_niveles(arbol.raiz)  # Resultado: 10 5 15 2 7
