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
        # Verifica que el nuevo enlace sea un objeto Link o None
        if link is None or isinstance(link, Link):
            self.__next = link
        else:
            raise Exception("El siguiente enlace debe ser un Link o None")

    def isLast(self):  # Verifica si este nodo es el último en la cadena
        return self.getNext() is None  # True si y solo si no hay un siguiente nodo

    def __str__(self):  # Crea una representación en cadena de este nodo
        return str(self.getData())  # Convierte el dato a cadena y lo retorna
