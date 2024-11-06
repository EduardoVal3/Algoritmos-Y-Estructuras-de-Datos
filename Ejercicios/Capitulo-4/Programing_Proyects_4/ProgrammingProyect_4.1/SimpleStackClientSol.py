from SimpleStack import *

stack = Stack(10)

try:
    # Insertar 10 elementos en la pila
    for word in ['May', 'the', 'force', 'be', 'with', 'you', 'always', 'find', 'the', 'way']:
        stack.push(word)
    print('Después de insertar', len(stack), 'elementos en la pila, contiene:\n', stack)
    print('¿Está la pila llena?', stack.isFull())

    # Intentar insertar otro elemento en una pila llena
    stack.push('extra')
except Exception as e:
    print(e)

try:
    print('Extrayendo elementos de la pila:')
    while not stack.isEmpty():
        print(stack.pop(), end=' ')
    print()
    
    # Intentar extraer un elemento de una pila vacía
    stack.pop()
except Exception as e:
    print(e)
