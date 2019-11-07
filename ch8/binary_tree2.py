class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(node):
    if node.left is not None:
        inorder(node.left)
    print(node.data)
    if node.right is not None:
        inorder(node.right)

from collections import deque
def bfs(node):
    stack = deque()

    while stack:
        node = stack.popleft()
        print(node.data)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# inorder(root)
bfs(root)