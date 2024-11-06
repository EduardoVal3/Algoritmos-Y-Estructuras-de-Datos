from LinkedList import LinkedList, Link

def main():
    # Crear una lista enlazada
    linked_list = LinkedList()
    
    # Crear algunos enlaces (nodos) e insertarlos en la lista
    node1 = Link(10)
    node2 = Link(20)
    node3 = Link(30)
    
    linked_list.setFirst(node1)  # Establecer el primer enlace
    node1.setNext(node2)  # Enlazar el primer nodo al segundo
    node2.setNext(node3)  # Enlazar el segundo nodo al tercero

    # Probar el método __len__ para obtener la longitud de la lista
    print("La longitud de la lista es:", len(linked_list))  # Debería ser 3

    # Probar el método __str__ para obtener la representación en cadena de la lista
    print("Contenido de la lista enlazada:", str(linked_list))  # Debería mostrar 10 > 20 > 30

    # Probar el método traverse con el iterador para aplicar una función a cada elemento
    print("Recorrido de la lista usando traverse:")
    linked_list.traverse(lambda x: print(f"Elemento: {x}"))  # Imprime cada elemento en la lista

# Llamar a la función principal para ejecutar el cliente
if __name__ == "__main__":
    main()