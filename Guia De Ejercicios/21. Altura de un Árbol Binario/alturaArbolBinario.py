# 21
import arbolBinario

def altura_arbol(nodo):
    if nodo is None:
        return 0  # Altura de un árbol vacío es 0
    izquierda = altura_arbol(nodo.izquierda)
    derecha = altura_arbol(nodo.derecha)
    return 1 + max(izquierda, derecha)

# Ejemplo de uso
arbol = arbolBinario()
for val in [10, 5, 15, 2, 7]:
    arbol.insertar(val)

print(altura_arbol(arbol.raiz))  # Resultado: 3 (si consideramos la raíz como nivel 1)
