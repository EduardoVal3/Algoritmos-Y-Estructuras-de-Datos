# Implementación de una estructura de datos tipo Array con métodos de ordenamiento
class Array(object):
    def __init__(self, initialSize):  # Constructor de la clase
        # Crear un arreglo de tamaño inicial con elementos `None`
        self.__a = [None] * initialSize
        # Al inicio no hay elementos en el arreglo
        self.__nItems = 0

    def __len__(self):  # Definir la función especial para `len()`
        # Retornar el número actual de elementos en el arreglo
        return self.__nItems

    def get(self, n):  # Retorna el valor en el índice `n`
        # Verifica si `n` está dentro de los límites válidos y retorna el valor solo si es así
        if 0 <= n < self.__nItems:
            return self.__a[n]

    def set(self, n, value):  # Establece el valor en el índice `n`
        # Verifica si `n` está dentro de los límites válidos y asigna el valor solo si es así
        if 0 <= n < self.__nItems:
            self.__a[n] = value

    def swap(self, j, k):  # Intercambia los valores en los índices `j` y `k`
        # Verifica si ambos índices están dentro de los límites antes de procesar
        if (0 <= j < self.__nItems and 0 <= k < self.__nItems):
            # Intercambia los elementos
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def insert(self, item):  # Inserta un elemento al final del arreglo
        # Si el arreglo está lleno, lanza una excepción
        if self.__nItems >= len(self.__a):
            raise Exception("Array overflow")
        # Coloca el nuevo elemento al final del arreglo
        self.__a[self.__nItems] = item
        # Incrementa el conteo de elementos
        self.__nItems += 1

    def find(self, item):  # Busca el índice de un elemento en el arreglo
        # Recorre los elementos actuales
        for j in range(self.__nItems):
            if self.__a[j] == item:  # Si encuentra el elemento, retorna el índice
                return j
        return -1  # Si no se encuentra, retorna -1

    def search(self, item):  # Busca un elemento y retorna su valor si existe
        # Llama al método `find()` y retorna el valor si lo encuentra
        return self.get(self.find(item))

    def delete(self, item):  # Elimina la primera ocurrencia de un elemento
        # Recorre los elementos actuales
        for j in range(self.__nItems):
            if self.__a[j] == item:  # Si encuentra el elemento
                self.__nItems -= 1  # Reduce el conteo de elementos
                for k in range(j, self.__nItems):  # Mueve los elementos a la izquierda
                    self.__a[k] = self.__a[k+1]
                return True  # Retorna éxito si se eliminó
        return False  # Retorna False si no se encontró el elemento

    def traverse(self, function=print):  # Recorre todos los elementos
        # Aplica la función dada a cada elemento en el arreglo
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):  # Definir la función especial para `str()`
        # Rodea los elementos con corchetes y separa con comas
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__a[i])
        ans += "]"
        return ans

    def bubbleSort(self):  # Ordena comparando valores adyacentes
        # Recorre los elementos desde el final hasta el inicio
        for last in range(self.__nItems-1, 0, -1):
            # El bucle interno recorre hasta el índice `last`
            for inner in range(last):
                # Si el elemento actual es mayor que el siguiente, los intercambia
                if self.__a[inner] > self.__a[inner+1]:
                    self.swap(inner, inner+1)

    def selectionSort(self):  # Ordena seleccionando el mínimo y colocándolo a la izquierda
        # Recorre desde el inicio hasta el penúltimo elemento
        for outer in range(self.__nItems-1):
            min = outer  # Suponemos que el mínimo es el primer elemento
            for inner in range(outer+1, self.__nItems):  # Busca hacia la derecha
                if self.__a[inner] < self.__a[min]:  # Si encuentra un nuevo mínimo, lo actualiza
                    min = inner
            self.swap(outer, min)  # Intercambia el mínimo con el elemento actual

    def insertionSort(self):  # Ordena mediante inserciones repetidas
        # Comienza desde el segundo elemento y recorre el arreglo
        for outer in range(1, self.__nItems):
            temp = self.__a[outer]  # Almacena el elemento actual
            inner = outer  # El bucle interno comienza en la posición `outer`
            while inner > 0 and temp < self.__a[inner-1]:  # Mientras el elemento sea menor
                self.__a[inner] = self.__a[inner-1]  # Desplaza los elementos a la derecha
                inner -= 1
            self.__a[inner] = temp  # Coloca el elemento en su posición correcta

    def median(self):  # Método para calcular la mediana
        # Si el arreglo está vacío, devolver None
        if self.__nItems == 0:
            return None

        # Hacemos una copia del arreglo y lo ordenamos
        sorted_array = sorted(self.__a[:self.__nItems])

        # Calculamos la posición del elemento central
        mid = self.__nItems // 2

        # Si el número de elementos es impar, la mediana es el elemento central
        if self.__nItems % 2 == 1:
            return sorted_array[mid]

        # Si el número de elementos es par, la mediana es el promedio de los dos centrales
        else:
            return (sorted_array[mid - 1] + sorted_array[mid]) / 2
