class BinarySearchTree:
    class __Node:
        def __init__(self, key, data, left=None, right=None):
            self.key = key
            self.data = data
            self.leftChild = left
            self.rightChild = right

        def __str__(self):
            return f"{{{self.key}, {self.data}}}"

    def __init__(self):
        self.__root = None

    def isEmpty(self):
        return self.__root is None

    def root(self):
        if self.isEmpty():
            raise Exception("No root node in empty tree")
        return (self.__root.data, self.__root.key)

    def __find(self, goal):
        current = self.__root
        parent = self
        while current and goal != current.key:
            parent = current
            current = current.leftChild if goal < current.key else current.rightChild
        return current, parent

    def search(self, goal):
        node, _ = self.__find(goal)
        return node.data if node else None

    def insert(self, key, data):
        node, parent = self.__find(key)
        if node:
            node.data = data
            return False
        if parent is self:
            self.__root = self.__Node(key, data)
        elif key < parent.key:
            parent.leftChild = self.__Node(key, data)
        else:
            parent.rightChild = self.__Node(key, data)
        return True

    def __inOrderTraverse(self, node, function):
        if node:
            self.__inOrderTraverse(node.leftChild, function)
            function(node)
            self.__inOrderTraverse(node.rightChild, function)

    def inOrderTraverse(self, function=print):
        self.__inOrderTraverse(self.__root, function)

    def __delete(self, parent, node):
        deleted = node.data
        if node.leftChild:
            if node.rightChild:
                self.__promote_successor(node)
            else:
                if parent is self:
                    self.__root = node.leftChild
                elif parent.leftChild is node:
                    parent.leftChild = node.leftChild
                else:
                    parent.rightChild = node.leftChild
        else:
            if parent is self:
                self.__root = node.rightChild
            elif parent.leftChild is node:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
        return deleted

    def __promote_successor(self, node):
        successor = node.rightChild
        parent = node
        while successor.leftChild:
            parent = successor
            successor = successor.leftChild
        node.key = successor.key
        node.data = successor.data
        self.__delete(parent, successor)

    def delete(self, goal):
        node, parent = self.__find(goal)
        if node is not None:
            return self.__delete(parent, node)
        return None

    def levels(self):
        return self.__levels(self.__root)

    def __levels(self, node):
        if node:
            return 1 + max(self.__levels(node.leftChild), self.__levels(node.rightChild))
        return 0

    def nodes(self):
        count = 0
        for _, _ in self.traverse():
            count += 1
        return count

    def traverse(self, traverseType='in'):
        if traverseType not in ['pre', 'in', 'post']:
            raise ValueError("Unknown traversal type: " + str(traverseType))
        return self.__traverse(self.__root, traverseType)

    def __traverse(self, node, traverseType):
        if node is None:
            return
        if traverseType == "pre":
            yield (node.key, node.data)
        yield from self.__traverse(node.leftChild, traverseType)
        if traverseType == "in":
            yield (node.key, node.data)
        yield from self.__traverse(node.rightChild, traverseType)
        if traverseType == "post":
            yield (node.key, node.data)

    def print(self, indentBy=4):
        self.__pTree(self.__root, "ROOT: ", "", indentBy)

    def __pTree(self, node, nodeType, indent, indentBy=4):
        if node:
            self.__pTree(node.rightChild, "RIGHT: ", indent + " " * indentBy, indentBy)
            print(indent + nodeType, node)
            self.__pTree(node.leftChild, "LEFT: ", indent + " " * indentBy, indentBy)
