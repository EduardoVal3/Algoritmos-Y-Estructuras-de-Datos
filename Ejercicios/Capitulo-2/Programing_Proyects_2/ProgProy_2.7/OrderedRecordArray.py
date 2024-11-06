def identity(x):  # Función identidad para clave predeterminada
    return x

class OrderedRecordArray:
    def __init__(self, initialSize, key=identity, growthFactor=1.5, fixedIncrement=None):
        """
        Constructor de la clase OrderedRecordArray.
        
        Parámetros:
        - initialSize: tamaño inicial del array.
        - key: función para obtener la clave de cada registro.
        - growthFactor: factor de crecimiento multiplicativo (si no se usa incremento fijo).
        - fixedIncrement: incremento fijo para crecimiento aditivo (si no se usa factor de crecimiento).
        """
        self.__a = [None] * initialSize  # El array almacenado como lista
        self.__nItems = 0  # Sin elementos inicialmente
        self.__key = key  # Función clave para ordenar los elementos
        self.__maxSize = initialSize  # Tamaño máximo inicial
        self.__growthFactor = growthFactor  # Factor de crecimiento multiplicativo
        self.__fixedIncrement = fixedIncrement  # Incremento fijo para crecimiento aditivo

    def __len__(self):
        return self.__nItems

    def get(self, n):
        if n >= 0 and n < self.__nItems:
            return self.__a[n]
        raise IndexError("Índice fuera de rango")

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__a[i])
        ans += "]"
        return ans

    def __resize(self):
        """
        Redimensiona el array cuando alcanza su capacidad máxima.
        - Si se especifica un incremento fijo, se utiliza para aumentar el tamaño.
        - De lo contrario, se utiliza el factor de crecimiento multiplicativo.
        """
        if self.__fixedIncrement is not None:  # Estrategia de crecimiento fijo
            newSize = self.__maxSize + self.__fixedIncrement
        else:  # Estrategia de crecimiento multiplicativo
            newSize = int(self.__maxSize * self.__growthFactor)

        newArray = [None] * newSize  # Crea un nuevo array con el tamaño expandido
        for i in range(self.__nItems):
            newArray[i] = self.__a[i]  # Copia los elementos actuales
        self.__a = newArray
        self.__maxSize = newSize  # Actualiza el tamaño máximo

    def insert(self, item):
        """
        Inserta un elemento en la posición correcta según la clave.
        Redimensiona el array si se alcanza su capacidad máxima.
        """
        if self.__nItems >= self.__maxSize:
            self.__resize()  # Redimensiona si el array está lleno

        j = self.find(self.__key(item))  # Encuentra la posición de inserción
        for k in range(self.__nItems, j, -1):
            self.__a[k] = self.__a[k - 1]  # Mueve los elementos mayores a la derecha
        self.__a[j] = item
        self.__nItems += 1  # Incrementa el número de elementos

    def find(self, key):
        """
        Encuentra el índice en o justo por debajo de la clave.
        Devuelve el índice de inserción si no se encuentra.
        """
        lo = 0
        hi = self.__nItems - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.__key(self.__a[mid]) == key:
                return mid
            elif self.__key(self.__a[mid]) < key:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo  # Punto de inserción si el elemento no se encuentra

    def delete(self, item):
        """
        Elimina la primera ocurrencia de un elemento.
        Devuelve True si se eliminó con éxito, False si no se encontró.
        """
        j = self.find(self.__key(item))
        if j < self.__nItems and self.__a[j] == item:
            self.__nItems -= 1
            for k in range(j, self.__nItems):
                self.__a[k] = self.__a[k + 1]  # Mueve los elementos mayores a la izquierda
            return True
        return False
    
    def merge(self, other):  # Fusiona otra matriz ordenada en la actual
        # Verifica si ambas matrices usan la misma función clave
        if self.__key != other._OrderedRecordArray__key:
            raise ValueError("Las funciones clave no coinciden. No se puede fusionar.")

        # Crea un nuevo arreglo suficientemente grande
        merged_array = [None] * (self.__nItems + other._OrderedRecordArray__nItems)
        
        i, j, k = 0, 0, 0  # Índices para self, other y merged_array

        # Realiza la mezcla ordenada
        while i < self.__nItems and j < other._OrderedRecordArray__nItems:
            if self.__key(self.__a[i]) <= self.__key(other._OrderedRecordArray__a[j]):
                merged_array[k] = self.__a[i]
                i += 1
            else:
                merged_array[k] = other._OrderedRecordArray__a[j]
                j += 1
            k += 1

        # Copia los elementos restantes de la matriz actual
        while i < self.__nItems:
            merged_array[k] = self.__a[i]
            i += 1
            k += 1

        # Copia los elementos restantes de la matriz de origen
        while j < other._OrderedRecordArray__nItems:
            merged_array[k] = other._OrderedRecordArray__a[j]
            j += 1
            k += 1

        # Actualiza el arreglo actual con los elementos fusionados
        self.__a = merged_array
        self.__nItems = k  # Actualiza el número total de elementos


    def delete2(self, item):  # Elimina todas las ocurrencias del elemento
        key = self.__key(item)
        index = self.find(key)  # Encuentra el índice de la clave o el punto de inserción

        if index >= self.__nItems or self.__key(self.__a[index]) != key:
            return False  # Si no se encuentra, no hace nada y devuelve False

        # Si encuentra el elemento, elimina todas las ocurrencias
        num_deleted = 0  # Contador para el número de elementos eliminados
        while index < self.__nItems and self.__key(self.__a[index]) == key:
            if self.__a[index] == item:
                # Elimina el elemento moviendo los elementos mayores a la izquierda
                for k in range(index, self.__nItems - 1):
                    self.__a[k] = self.__a[k + 1]
                self.__nItems -= 1  # Reduce el número de elementos
                num_deleted += 1
            else:
                index += 1  # Si el elemento no coincide exactamente, avanza

        return num_deleted > 0  # Devuelve True si al menos un elemento fue eliminado
