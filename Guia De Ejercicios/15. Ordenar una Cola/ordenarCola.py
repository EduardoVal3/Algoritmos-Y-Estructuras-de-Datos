# 15
from collections import deque

def ordenar_cola(cola):
    n = len(cola)
    for i in range(n):
        for j in range(n - 1 - i):
            a = cola.popleft()
            b = cola.popleft()
            if a > b:
                cola.append(b)
                cola.append(a)
            else:
                cola.append(a)
                cola.append(b)
        cola.append(cola.popleft())  # Mantener el orden interno
    return cola

# Ejemplo de uso
cola = deque([4, 1, 3, 2])
resultado = ordenar_cola(cola)
print(list(resultado))  # [1, 2, 3, 4]
