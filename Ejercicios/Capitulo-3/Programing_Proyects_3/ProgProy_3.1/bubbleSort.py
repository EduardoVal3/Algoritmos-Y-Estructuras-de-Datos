def bubbleSortBidirectional(self):
    left = 0  # índice exterior izquierdo
    right = self.__nItems - 1  # índice exterior derecho

    while left < right:
        # Paso de izquierda a derecha: encontrar el elemento más grande y llevarlo al final
        for i in range(left, right):
            if self.__a[i] > self.__a[i + 1]:
                self.swap(i, i + 1)
        
        # Reducir el límite derecho, ya que el elemento mayor está en su lugar
        right -= 1

        # Paso de derecha a izquierda: encontrar el elemento más pequeño y llevarlo al inicio
        for i in range(right, left, -1):
            if self.__a[i] < self.__a[i - 1]:
                self.swap(i, i - 1)
        
        # Aumentar el límite izquierdo, ya que el elemento menor está en su lugar
        left += 1
