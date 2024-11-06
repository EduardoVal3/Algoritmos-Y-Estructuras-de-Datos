def identity(x):  # Función identidad
    return x

class OrderedRecordArray(object):
    def __init__(self, initialSize, key=identity):  # Constructor
        self.__a = [None] * initialSize  # El array se almacena como una lista
        self.__nItems = 0  # Inicialmente no hay elementos en el array
        self.__key = key  # La función clave obtiene la clave del registro

    def __len__(self):  # Método especial para la función len()
        return self.__nItems  # Devuelve el número de elementos

    def get(self, n):  # Devuelve el valor en el índice n
        if n >= 0 and n < self.__nItems:  # Verifica si n está dentro de los límites
            return self.__a[n]  # Solo devuelve el elemento si está en los límites
        raise IndexError("Índice " + str(n) + " fuera de rango")

    def traverse(self, function=print):  # Recorre todos los elementos
        for j in range(self.__nItems):  # y aplica una función a cada uno
            function(self.__a[j])

    def __str__(self):  # Método especial para la función str()
        ans = "["  # Rodea la cadena con corchetes
        for i in range(self.__nItems):  # Recorre todos los elementos
            if len(ans) > 1:  # Excepto junto al corchete izquierdo,
                ans += ", "  # separa los elementos con comas
            ans += str(self.__a[i])  # Agrega la representación en cadena del elemento
        ans += "]"  # Cierra con el corchete derecho
        return ans

    def find(self, key):  # Encuentra el índice de la clave o el punto de inserción
        lo = 0  # en una lista ordenada
        hi = self.__nItems - 1  # Busca entre los límites lo y hi
        while lo <= hi:
            mid = (lo + hi) // 2  # Selecciona el punto medio
            if self.__key(self.__a[mid]) == key:  # ¿Encontramos la clave?
                return mid  # Devuelve la ubicación del elemento
            elif self.__key(self.__a[mid]) < key:  # ¿Está la clave en la mitad superior?
                lo = mid + 1  # Sí, aumenta el límite inferior
            else:
                hi = mid - 1  # No, pero podría estar en la mitad inferior
        return lo  # Elemento no encontrado, devuelve el punto de inserción

    def search(self, key):
        idx = self.find(key)  # Busca un registro por su clave
        if idx < self.__nItems and self.__key(self.__a[idx]) == key:
            return self.__a[idx]  # Devuelve el elemento si se encuentra

    def insert(self, item):  # Inserta un elemento en la posición correcta
        if self.__nItems >= len(self.__a):  # Si el array está lleno,
            raise Exception("Array overflow")  # lanza una excepción
        j = self.find(self.__key(item))  # Encuentra dónde debería ir el elemento
        for k in range(self.__nItems, j, -1):  # Mueve los elementos mayores a la derecha
            self.__a[k] = self.__a[k - 1]
        self.__a[j] = item  # Inserta el elemento
        self.__nItems += 1  # Incrementa el número de elementos

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


    def delete(self, item):  # Elimina todas las ocurrencias del elemento
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
