# Ejercicio 9.
# Simula una calculadora que use una pila para realizar operaciones básicas (+, -, *, /). Los números y operaciones se ingresan como una lista.

def calculadora_pila(operaciones):
    pila = []
    for item in operaciones:
        if isinstance(item, (int, float)):
            pila.append(item)
        else:
            b = pila.pop()
            a = pila.pop()
            if item == '+':
                pila.append(a + b)
            elif item == '-':
                pila.append(a - b)
            elif item == '*':
                pila.append(a * b)
            elif item == '/':
                pila.append(a / b)
    return pila.pop()

# Ejemploo
operaciones = [3, 4, '+', 2, '*', 7, '/']
print(calculadora_pila(operaciones))  # 2.0
