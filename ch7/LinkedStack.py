class EmptyException(Exception):
    pass


class LinkedStack:
    class _Node:
        def __init__(self, e, next):
            self._element = e
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise EmptyException('Queue is empty!')
        ans = self._head._element
        self._head = self._head._next
        self._size -= 1
        return ans

    def top(self):
        if self._size == 0:
            raise EmptyException('Queue is empty!')
        return self._head._element
