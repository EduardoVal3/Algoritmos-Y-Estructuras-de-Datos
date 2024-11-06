class Link(object):  # Un nodo en una lista enlazada
    def __init__(self, datum, next=None):  # Constructor
        self.__data = datum  # El dato para este nodo
        self.__next = next  # Referencia al siguiente nodo (Link)

    def getData(self):  # Retorna el dato almacenado en este nodo
        return self.__data

    def setData(self, datum):  # Cambia el dato en este nodo
        self.__data = datum

    def getNext(self):  # Retorna el siguiente nodo (Link)
        return self.__next

    def setNext(self, link):  # Cambia el siguiente nodo por un nuevo Link
        if link is None or isinstance(link, Link):
            self.__next = link
        else:
            raise Exception("El siguiente enlace debe ser un Link o None")

    def isLast(self):  # Verifica si este nodo es el último en la cadena
        return self.getNext() is None  # True si y solo si no hay un siguiente nodo

    def __str__(self):  # Crea una representación en cadena de este nodo
        return str(self.getData())

class LinkedList(object):  # Clase lista enlazada
    def __init__(self):  # Constructor
        self.__first = None  # Primer enlace (inicio de la lista)

    def getFirst(self):  # Retorna el primer enlace
        return self.__first

    def setFirst(self, link):  # Cambia el primer enlace de la lista
        if link is None or isinstance(link, Link):
            self.__first = link
        else:
            raise Exception("El primer enlace debe ser un Link o None")

    def __iter__(self):  # Definir el iterador para recorrer la lista
        current = self.getFirst()  # Comenzamos desde el primer enlace
        while current is not None:  # Mientras haya enlaces
            yield current.getData()  # Devolvemos los datos del enlace
            current = current.getNext()  # Nos movemos al siguiente enlace

    def traverse(self, func=print):  # Recorre la lista y aplica una función a cada elemento
        for data in self:  # Usamos el iterador
            func(data)

    def __len__(self):  # Obtiene la longitud de la lista
        length = 0
        for _ in self:  # Usamos el iterador para contar los elementos
            length += 1
        return length

    def __str__(self):  # Crea una representación en cadena de la lista
        return " > ".join(str(data) for data in self)  # Usamos el iterador para convertir los datos en cadena
