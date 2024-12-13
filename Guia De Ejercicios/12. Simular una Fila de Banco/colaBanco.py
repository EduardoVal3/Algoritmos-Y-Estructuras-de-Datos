# 
# Usa una cola para simular la atención al cliente en un banco. Cada cliente tiene un número asignado y se atiende en orden.

from collections import deque

def fila_banco(clientes):
    fila = deque(clientes)
    while fila:
        cliente = fila.popleft()
        print(f"Atendiendo al cliente {cliente}")

# Ejemplo 
fila_banco([1, 2, 3])
