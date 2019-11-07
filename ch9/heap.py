class Empty(Exception):
    pass


class PriorityQueueBase:
    class _Item:
        __slots__ = '_key', '_value', '_sort_key'

        def __init__(self, key, value, sort_key=None):
            self._key = key
            self._value = value
            self._sort_key = sort_key

        def __lt__(self, other):
            if self._sort_key is not None:
                return self._sort_key(self._key) < self._sort_key(other._key)
            else:
                return self._key < other._key

    def is_empty(self):
        return len(self) == 0


class HeapPriorityQueue(PriorityQueueBase):
    # Non public behaviors

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            smaller = self._left(j)
            if self._has_right(j):
                smaller = self._left(j) if self._data[self._left(j)] < self._data[self._right(j)] else self._right(j)
            if self._data[smaller] < self._data[j]:
                self._swap(j, smaller)
                self._downheap(smaller)

    # Public behaviors
    def __init__(self, sort_key=None):
        self._data = []
        self.sort_key = sort_key

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.append(self._Item(key, value, self.sort_key))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        return self._data[0]._key, self._data[0]._value

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        key, value = self.min()
        self._data[0] = self._data[-1]
        del self._data[-1]
        self._downheap(0)

        return key, value


class AdaptableHeapPriorityQueue(HeapPriorityQueue):

    class Locator(HeapPriorityQueue._Item):
        __slots__ = '_idx'

        def __init__(self, key, value, idx):
            super.__init__(key, value)
            self._idx = idx

    def _swap(self, i, j):
        super._swap(i, j)
        # self._data[i]._idx = i
        # self._data[j]._idx = j
        self._data[i]._idx, self._data[j]._idx = self._data[j]._idx, self._data[i]._idx

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, key, value):
        token = self._Locator(key, value, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)

        return token

    def update(self, loc, newkey, newval):
        idx = loc._idx
        if not (0 <= idx < len(self) and self._data[idx] is loc):
            raise ValueError('Invalid locator')

        loc._key = newkey
        loc._val = newval
        self._bubble(idx)

    def remove(self, loc):
        idx = loc._idx
        if not (0 <= idx < len(self) and self._data[idx] is loc):
            raise ValueError('Invalid locator')

        if idx == len(self) - 1:
            self._data.pop()
        else:
            self._swap(idx, len(self) - 1)
            self._data.pop()
            self._bubble(idx)

        return loc._key, loc._value
