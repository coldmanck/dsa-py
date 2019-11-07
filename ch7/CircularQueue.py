class EmptyException(Exception):
    pass


class CircularQueue:
    class _Node:
        def __init__(self, e, next):
            self._element = e
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise EmptyException('Empty queue!')
        return self._tail._next._element

    def enqueue(self, e):
        if self.is_empty():
            newest = self._Node(e, None)
            newest._next = newest
        else:
            newest = self._Node(e, self._tail._next)
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyException('Empty queue!')
        ans = self._tail._next._element
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = self._tail._next._next
        self._size -= 1
        return ans

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next