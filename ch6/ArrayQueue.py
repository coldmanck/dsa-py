class EmptyException(Exception):
    pass


class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        if self.is_empty():
            return EmptyException('Stack is empty!')
        else:
            if (self._front + self._size) <= len(self._data):
                ans = str(self._data[self._front:self._front + self._size])
            else:
                ans = str(self._data[self._front:] + self._data[:self._front + self._size % len(self._data)])
            return ans

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise EmptyException('Queue is empty!')

        return self._data[self._front]

    def enqueue(self, item):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        idx = (self._front + self._size) % len(self._data)
        self._data[idx] = item
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyException('Queue is empty!')
        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        if self._size <= int(len(self._data) / 4):
            self._resize(int(len(self._data) / 2))

        return item

    def _resize(self, new_size):
        old = self._data
        self._data = [None] * new_size
        for i in range(self._size):
            old_idx = (self._front + i) % len(old)
            self._data[i] = old[old_idx]
        self._front = 0
