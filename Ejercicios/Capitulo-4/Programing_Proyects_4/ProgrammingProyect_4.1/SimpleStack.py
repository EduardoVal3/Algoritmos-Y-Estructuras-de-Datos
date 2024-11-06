# Implementar una estructura de datos de Pila usando una lista de Python

class Stack(object):
    def __init__(self, max): # Constructor
        self.__stackList = [None] * max # La pila almacenada como una lista
        self.__top = -1 # No hay elementos inicialmente
    
    def push(self, item): # Insertar elemento en la parte superior de la pila
        if self.isFull():
            raise Exception("Desbordamiento de pila: intentando insertar en una pila llena")
        self.__top += 1 # Avanzar el puntero
        self.__stackList[self.__top] = item # Almacenar el elemento
    
    def pop(self): # Eliminar el elemento superior de la pila
        if self.isEmpty():
            raise Exception("Subdesbordamiento de pila: intentando extraer de una pila vacía")
        top = self.__stackList[self.__top] # Elemento superior
        self.__stackList[self.__top] = None # Eliminar referencia al elemento
        self.__top -= 1 # Disminuir el puntero
        return top # Devolver el elemento superior
    
    def peek(self): # Devolver el elemento superior
        if not self.isEmpty(): # Si la pila no está vacía
            return self.__stackList[self.__top] # Devolver el elemento superior
    
    def isEmpty(self): # Verificar si la pila está vacía
        return self.__top < 0
    
    def isFull(self): # Verificar si la pila está llena
        return self.__top >= len(self.__stackList) - 1
    
    def __len__(self): # Devolver el número de elementos en la pila
        return self.__top + 1
    
    def __str__(self): # Convertir la pila a cadena de texto
        ans = "[" # Comenzar con corchete izquierdo
        for i in range(self.__top + 1): # Recorrer los elementos actuales
            if len(ans) > 1: # Excepto junto al corchete izquierdo,
                ans += ", " # separar elementos con coma
            ans += str(self.__stackList[i]) # Añadir la forma de cadena del elemento
        ans += "]" # Cerrar con corchete derecho
        return ans
