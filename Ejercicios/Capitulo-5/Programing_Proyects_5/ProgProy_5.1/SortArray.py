import Link

class LinkedList(object):  # Una lista enlazada de elementos de datos
    def __init__(self):  # Constructor
        self.__first = None  # Referencia al primer nodo (Link)

    def getFirst(self):
        return self.__first  # Retorna el primer nodo (Link)

    def setFirst(self, link):  # Cambia el primer nodo (Link)
        # Asegura que el primer nodo sea un objeto Link o None
        if link is None or isinstance(link, Link):
            self.__first = link
        else:
            raise Exception("El primer nodo debe ser un Link o None")

    def getNext(self):
        return self.getFirst()  # El primer nodo es el siguiente

    def setNext(self, link):
        self.setFirst(link)  # El primer nodo es el siguiente

    def isEmpty(self):  # Verifica si la lista está vacía
        return self.getFirst() is None  # True si no hay primer nodo

    def first(self):  # Retorna el primer elemento en la lista
        if self.isEmpty():  # Solo si no está vacía
            raise Exception('No hay primer elemento en la lista vacía')
        return self.getFirst().getData()  # Retorna el dato del primer nodo

    def __iter__(self):  # Define un iterador para la lista
        next = self.getFirst()  # Empieza con el primer nodo
        while next is not None:  # Mientras el nodo no sea None
            yield next.getData()  # Yields el dato del nodo
            next = next.getNext()  # Luego pasa al siguiente nodo

    def traverse(self, func=print):  # Aplica una función a todos los elementos de la lista
        for data in self:  # Utiliza el iterador para recorrer la lista
            func(data)  # Aplica la función (por defecto print)

    def __len__(self):  # Retorna la longitud de la lista
        return sum(1 for _ in self)  # Cuenta los elementos usando el iterador

    def __str__(self):  # Crea una representación en cadena de la lista
        return "[" + " > ".join(str(data) for data in self) + "]"  # Une los datos con " > " y los rodea con corchetes
