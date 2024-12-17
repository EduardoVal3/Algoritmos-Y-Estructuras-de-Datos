# 14

from collections import deque

def reorganizar_cola(cola):
    pares = deque()
    impares = deque()
    while cola:
        elemento = cola.popleft()
        if elemento % 2 == 0:
            pares.append(elemento)
        else:
            impares.append(elemento)
    return pares + impares

# Ejemplo de uso
cola = deque([1, 2, 3, 4, 5, 6])
resultado = reorganizar_cola(cola)
print(list(resultado))  # [2, 4, 6, 1, 3, 5]
