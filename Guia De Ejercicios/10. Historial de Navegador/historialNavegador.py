# Ejercicio 10.
# Implementa una pila para simular el historial de navegación en un navegador. Agrega una operación para “ir hacia atrás”.

class Historial:
    def __init__(self):
        self.historial = []

    def visitar(self, url):
        self.historial.append(url)

    def ir_atras(self):
        return self.historial.pop() if self.historial else None

# Ejemplo de uso
historial = Historial()
historial.visitar("pagina1.com")
historial.visitar("pagina2.com")
print(historial.ir_atras())  # "pagina2.com"
