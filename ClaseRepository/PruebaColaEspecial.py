class ColaEspecial():
    def __init__(self, max_size=10):
         self.cola = [None] * max_size
         self.max_size = max_size
         self.size = 0
         self.current_index = 0
         self.direccion = 1
    
    def insertar(self, elemento):
        if self.size < self.max_size:
            self.cola[self.size] = elemento
            self.size += 1
        else:
            self.cola[self.current_index] = elemento
            self.current_index += self.direccion
            if self.current_index >= self.max_size:
                self.current_index = self.max_size - 1
                self.direccion = -1
            elif self.current_index < 0:
                self.current_index = 0
                self.direccion = 1
                
    def mostrar_cola(self):
        return ''.join([str(e) for e in self.cola if e is not None])

if __name__ == "__main__":
    cola_especial = ColaEspecial()
    secuencia = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
    
    for elemento in secuencia:
        cola_especial.insertar(elemento)
        
    print("Resultado:", cola_especial.mostrar_cola())   
                
                
                
