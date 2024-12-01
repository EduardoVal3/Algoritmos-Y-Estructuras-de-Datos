class BinarySearchTree:
    class Node:
        def __init__(self, key, data):
            self.key = key
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root_node = None

    def isEmpty(self):
        return self.root_node is None

    def __find(self, key, find_deepest=True):
        # Encuentra el nodo más profundo (o más superficial si `find_deepest` es False)
        parent, node, is_left = None, self.root_node, None
        target_parent, target_node = None, None

        while node:
            if node.key == key:
                target_parent, target_node = parent, node
                if not find_deepest:  # Devuelve la más superficial
                    break
            parent = node
            if key <= node.key:
                node, is_left = node.left, True
            else:
                node, is_left = node.right, False

        return target_parent, target_node, is_left

    def search(self, key, find_deepest=True):
        _, node, _ = self.__find(key, find_deepest)
        if node:
            return node.data
        return None

    def insert(self, key, data):
        new_node = self.Node(key, data)
        if self.isEmpty():
            self.root_node = new_node
            return

        parent, node, is_left = None, self.root_node, None

        while node:
            parent = node
            if key <= node.key:
                node, is_left = node.left, True
            else:
                node, is_left = node.right, False

        if key <= parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def __delete_deepest(self, key):
        # Borra el nodo más profundo con la clave dada
        parent, target, is_left = self.__find(key)
        if not target:
            return None

        if not target.left and not target.right:  # Nodo hoja
            if parent:
                if is_left:
                    parent.left = None
                else:
                    parent.right = None
            else:  # Raíz sin hijos
                self.root_node = None
            return target.data

        # Nodo con un hijo o más
        if target.left:
            successor = target.left
            target.key, target.data = successor.key, successor.data
            target.left = successor.left
        elif target.right:
            successor = target.right
            target.key, target.data = successor.key, successor.data
            target.right = successor.right

        return target.data

    def delete(self, key):
        return self.__delete_deepest(key)

    def __traverse(self, node, result, order):
        if not node:
            return
        if order == "pre":
            result.append((node.key, node.data))
        self.__traverse(node.left, result, order)
        if order == "in":
            result.append((node.key, node.data))
        self.__traverse(node.right, result, order)
        if order == "post":
            result.append((node.key, node.data))

    def traverse(self, order="in"):
        result = []
        self.__traverse(self.root_node, result, order)
        return result
