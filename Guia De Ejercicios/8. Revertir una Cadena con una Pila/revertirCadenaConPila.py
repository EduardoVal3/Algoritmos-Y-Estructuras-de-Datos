# Ejercicio 8.
# Escribe una función que use una pila para invertir una cadena de texto.

def revertir_cadena(cadena):
    pila = list(cadena)
    return ''.join([pila.pop() for _ in range(len(pila))])

# Ejemplo 
print(revertir_cadena("Hola"))  # "aloH"
