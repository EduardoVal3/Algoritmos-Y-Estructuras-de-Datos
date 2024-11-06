import Link
import SortArray

def main():
    # Crear una lista enlazada y agregar elementos
    linked_list = SortArray.LinkedList()
    
    # Añadir algunos datos de ejemplo
    linked_list.setFirst(Link(10))  # Primer elemento
    linked_list.getFirst().setNext(Link(20))  # Segundo elemento
    linked_list.getFirst().getNext().setNext(Link(30))  # Tercer elemento
    
    # Probar el método __len__ para obtener la longitud de la lista
    print("La longitud de la lista es:", len(linked_list))  # Debería ser 3

    # Probar el método __str__ para obtener la representación en cadena de la lista
    print("Contenido de la lista enlazada:", str(linked_list))  # Debería mostrar [10 > 20 > 30]

    # Probar el método traverse con el iterador para aplicar una función a cada elemento
    print("Recorrido de la lista usando traverse:")
    linked_list.traverse(lambda x: print(f"Elemento: {x}"))  # Imprime cada elemento en la lista

# Llamar a la función principal para ejecutar el cliente
if __name__ == "__main__":
    main()