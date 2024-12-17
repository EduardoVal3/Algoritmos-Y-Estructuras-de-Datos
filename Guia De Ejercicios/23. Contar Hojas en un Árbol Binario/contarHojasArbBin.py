# 23
import arbolBinario

def contar_hojas(nodo):
    if nodo is None:
        return 0  # Árbol vacío no tiene hojas
    if nodo.izquierda is None and nodo.derecha is None:
        return 1  # Nodo hoja encontrado
    return contar_hojas(nodo.izquierda) + contar_hojas(nodo.derecha)

# Ejemplo de uso
arbol = arbolBinario()
for val in [10, 5, 15, 2, 7]:
    arbol.insertar(val)

print(contar_hojas(arbol.raiz))  # Resultado: 3 (nodos hoja son: 2, 7, 15)
