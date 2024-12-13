# Ejercicio 7.
# Usa una pila para verificar si una cadena de paréntesis ((), {}, []) está balanceada.

def verificar_balance(cadena):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    for char in cadena:
        if char in '({[':
            pila.append(char)
        elif char in ')}]':
            if not pila or pila.pop() != pares[char]:
                return False

    return not pila

# Ejemplo
print(verificar_balance("{[()]}"))  # True
print(verificar_balance("{[(])}"))  # False
