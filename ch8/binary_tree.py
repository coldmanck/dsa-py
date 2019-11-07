class BinaryTree:
    class _Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self._root = None
        self._size = 0

    def is_empty(self):
        return self._root == None

    def add_root(self, data):
        self._root = self._Node(data)

    def add_left(self, pos, data):
        pos.left = self._Node(data)

    def add_right(self, pos, data):
        pos.right = self._Node(data)

    def preorder_traversal(self):
        self._preorder_traversal(self._root)

    def _preorder_traversal(self, pos):
        if pos.left is not None:
            self._preorder_traversal(pos.left)
        print(pos.data)
        if pos.right is not None:
            self._preorder_traversal(pos.right)

