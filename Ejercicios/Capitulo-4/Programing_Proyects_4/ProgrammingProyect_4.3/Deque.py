class Deque(object):
    def __init__(self, max_size):
        # Inicializa la deque con un tamaño máximo.
        self.__deque = [None] * max_size
        self.__max_size = max_size
        self.__left = 0  # Índice del extremo izquierdo de la deque
        self.__right = 0 # Índice del extremo derecho de la deque
        self.__size = 0  # Número de elementos en la deque

    def insertLeft(self, item):
        # Inserta un elemento en el extremo izquierdo de la deque.
        if self.isFull():
            raise Exception("Deque está llena")
        self.__left = (self.__left - 1) % self.__max_size  # Envolvimiento al final de la matriz
        self.__deque[self.__left] = item
        self.__size += 1

    def insertRight(self, item):
        # Inserta un elemento en el extremo derecho de la deque.
        if self.isFull():
            raise Exception("Deque está llena")
        self.__deque[self.__right] = item
        self.__right = (self.__right + 1) % self.__max_size  # Envolvimiento al final de la matriz
        self.__size += 1

    def removeLeft(self):
        # Elimina y devuelve el elemento del extremo izquierdo de la deque.
        if self.isEmpty():
            raise Exception("Deque está vacía")
        item = self.__deque[self.__left]
        self.__deque[self.__left] = None  # Elimina la referencia al elemento
        self.__left = (self.__left + 1) % self.__max_size  # Envolvimiento al final de la matriz
        self.__size -= 1
        return item

    def removeRight(self):
        # Elimina y devuelve el elemento del extremo derecho de la deque.
        if self.isEmpty():
            raise Exception("Deque está vacía")
        self.__right = (self.__right - 1) % self.__max_size  # Envolvimiento al final de la matriz
        item = self.__deque[self.__right]
        self.__deque[self.__right] = None  # Elimina la referencia al elemento
        self.__size -= 1
        return item

    def peekLeft(self):
        # Devuelve el elemento del extremo izquierdo sin eliminarlo.
        if self.isEmpty():
            raise Exception("Deque está vacía")
        return self.__deque[self.__left]

    def peekRight(self):
        # Devuelve el elemento del extremo derecho sin eliminarlo.
        if self.isEmpty():
            raise Exception("Deque está vacía")
        return self.__deque[(self.__right - 1) % self.__max_size]

    def isEmpty(self):
        # Verifica si la deque está vacía.
        return self.__size == 0

    def isFull(self):
        # Verifica si la deque está llena.
        return self.__size == self.__max_size

    def __len__(self):
        # Devuelve el número de elementos en la deque.
        return self.__size

    def __str__(self):
        # Devuelve una representación de cadena de la deque.
        return str([self.__deque[(self.__left + i) % self.__max_size] for i in range(self.__size)])
