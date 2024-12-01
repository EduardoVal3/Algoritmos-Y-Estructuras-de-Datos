
class BinaryTree:
    class Node:
        def __init__(self, value):
            self.value = value  # Valor del nodo (operador u operando)
            self.left = None  # Hijo izquierdo
            self.right = None  # Hijo derecho

    def __init__(self):
        self.root = None  # Nodo raíz del árbol

    def create_tree(self, value):
        """Crea un árbol con un único nodo."""
        self.root = self.Node(value)

    def combine_trees(self, operator, left_tree, right_tree):
        """Combina dos árboles binarios usando un operador como nodo raíz."""
        self.root = self.Node(operator)
        self.root.left = left_tree.root
        self.root.right = right_tree.root

    def preorder(self, node=None):
        """Recorrido previo (preorden)."""
        if node is None:
            node = self.root
        result = node.value
        if node.left:
            result += self.preorder(node.left)
        if node.right:
            result += self.preorder(node.right)
        return result

    def inorder(self, node=None):
        """Recorrido en orden (con paréntesis para priorizar operadores)."""
        if node is None:
            node = self.root
        result = ""
        if node.left:
            result += "(" + self.inorder(node.left)
        result += node.value
        if node.right:
            result += self.inorder(node.right) + ")"
        return result

    def postorder(self, node=None):
        """Recorrido posterior (postorden)."""
        if node is None:
            node = self.root
        result = ""
        if node.left:
            result += self.postorder(node.left)
        if node.right:
            result += self.postorder(node.right)
        result += node.value
        return result




class ExpressionTreeBuilder:
    def __init__(self):
        self.operators = set("+-*/")  # Conjunto de operadores válidos

    def build_tree(self, postfix_expression):
        """Construye un árbol binario a partir de una expresión sufija."""
        stack = []
        tokens = postfix_expression.split()  # Divide la cadena en tokens

        for token in tokens:
            if token not in self.operators:  # Si es operando
                tree = BinaryTree()
                tree.create_tree(token)  # Crea un árbol para el operando
                stack.append(tree)
            else:  # Si es operador
                if len(stack) < 2:  # Se necesitan al menos dos operandos
                    raise ValueError("Expresión sufija inválida")
                right_tree = stack.pop()
                left_tree = stack.pop()
                combined_tree = BinaryTree()
                combined_tree.combine_trees(token, left_tree, right_tree)
                stack.append(combined_tree)

        if len(stack) != 1:  # Debe quedar solo un árbol al final
            raise ValueError("Expresión sufija inválida")

        return stack.pop()  # Devuelve el árbol construido


def main():
    builder = ExpressionTreeBuilder()

    expressions = [
        "91 95 + 15 + 19 + 4 *",
        "B B * A C 4 * * -",
        "42",
        "A 57",  # Excepción
        "+ /"    # Excepción
    ]

    for i, expr in enumerate(expressions, start=1):
        print(f"Expresión {i}: {expr}")
        try:
            tree = builder.build_tree(expr)
            print("Preorden:", tree.preorder())
            print("En orden:", tree.inorder())
            print("Postorden:", tree.postorder())
        except ValueError as e:
            print("Error:", e)
        print()

print (main())
