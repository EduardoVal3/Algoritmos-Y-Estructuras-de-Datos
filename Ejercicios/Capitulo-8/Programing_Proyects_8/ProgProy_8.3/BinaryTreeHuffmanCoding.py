import heapq
from typing import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        """Inicializa un nodo del árbol de Huffman."""
        self.char = char        # El carácter almacenado en el nodo (None para nodos internos)
        self.freq = freq        # La frecuencia asociada al carácter o suma de frecuencias
        self.left = None        # Hijo izquierdo
        self.right = None       # Hijo derecho

    def __lt__(self, other):
        """Define la comparación entre nodos basada en la frecuencia."""
        return self.freq < other.freq

    def __eq__(self, other):
        """Define la igualdad entre nodos."""
        return self.freq == other.freq



class HuffmanCoding:
    def __init__(self):
        self.codes = {}         # Tabla de códigos: carácter -> código binario
        self.reverse_codes = {} # Tabla inversa: código binario -> carácter

    def build_tree(self, text):
        """Construye el árbol de Huffman a partir del texto."""
        # Calcular frecuencias de cada carácter
        frequency = Counter(text)

        # Crear una cola de prioridad (min-heap)
        heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
        heapq.heapify(heap)

        # Construir el árbol de Huffman
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = HuffmanNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            heapq.heappush(heap, merged)

        # El último nodo en el heap es la raíz del árbol
        return heap[0]

    def build_codes(self, root, current_code=""):
        """Genera la tabla de códigos a partir del árbol de Huffman."""
        if root is None:
            return

        # Si es una hoja, asigna el código al carácter
        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_codes[current_code] = root.char
            return

        # Recorrer el árbol en preorden para asignar códigos
        self.build_codes(root.left, current_code + "0")
        self.build_codes(root.right, current_code + "1")

    def encode(self, text):
        """Codifica el texto en binario usando la tabla de códigos."""
        return ''.join(self.codes[char] for char in text)

    def decode(self, encoded_text):
        """Decodifica el texto binario en texto original usando la tabla inversa."""
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_codes:
                decoded_text += self.reverse_codes[current_code]
                current_code = ""

        return decoded_text

    def display_tree(self, root, indent=""):
        """Muestra el árbol de Huffman en formato de texto."""
        if root is None:
            return
        if root.char:
            print(f"{indent}└─ '{root.char}' ({root.freq})")
        else:
            print(f"{indent}└─ ({root.freq})")
        self.display_tree(root.left, indent + "    ")
        self.display_tree(root.right, indent + "    ")





def main():
    # Entrada del usuario
    text = input("Introduce el mensaje de texto para codificar: ")

    # Crear instancia de HuffmanCoding
    huffman = HuffmanCoding()

    # Construir el árbol de Huffman
    root = huffman.build_tree(text)

    # Generar la tabla de códigos
    huffman.build_codes(root)

    # Codificar el mensaje
    encoded_text = huffman.encode(text)

    # Decodificar el mensaje
    decoded_text = huffman.decode(encoded_text)

    # Mostrar resultados
    print("\nTabla de códigos:")
    for char, code in huffman.codes.items():
        print(f"{repr(char)}: {code}")

    print("\nMensaje original:", text)
    print("Mensaje codificado:", encoded_text)
    print("Mensaje decodificado:", decoded_text)
    print(f"\nNúmero de caracteres en el mensaje original: {len(text)}")
    print(f"Número de bits en el mensaje codificado: {len(encoded_text)}")

    # Mostrar el árbol si el mensaje es corto
    if len(text) <= 10:
        print("\nÁrbol de Huffman:")
        huffman.display_tree(root)

if __name__ == "__main__":
    main()
