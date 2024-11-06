# Programa para determinar si una cadena es un palíndromo usando una pila
from SimpleStack import *

def is_palindrome(s):
    stack = Stack(len(s))  # Crear una pila del tamaño de la cadena
    sanitized_string = ''.join(char.lower() for char in s if char.isalpha())  # Normalizar la cadena

    for char in sanitized_string:
        stack.push(char)

    reversed_string = ''
    while not stack.isEmpty():
        reversed_string += stack.pop()

    return sanitized_string == reversed_string

# Ejemplo de uso
phrase = "Un hombre, un plan, un canal, Panamá"
if is_palindrome(phrase):
    print(f'"{phrase}" es un palíndromo.')
else:
    print(f'"{phrase}" no es un palíndromo.')
