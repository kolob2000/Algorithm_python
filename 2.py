class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)



class Tree:
    def __init__(self, value=None):
        self.root = Node(value)

    def _print(self):
        def __str(node: Node):
            print(f'{node}')

            if node.left:
                __str(node.left)
            if node.right:
                __str(node.right)

        __str(self.root)

    def add(self, value):
        def __new_leaf(value, node):
            if value > node.value and node.right is None:
                node.right = Node(value)
                return node.right.value
            elif value <= node.value and node.left is None:
                node.left = Node(value)
                return node.left.value
            elif value > node.value:
                return __new_leaf(value, node.right)
            else:
                return __new_leaf(value, node.left)

        # if isinstance(self.root, None):
        #     self.root = Node(value)
        #     return self.root.value
        # else:
        return __new_leaf(value, self.root)


tree = Tree(7)
tree.add(5)
tree.add(5)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(3)
tree.add(5)
tree.add(2)
tree._print()
