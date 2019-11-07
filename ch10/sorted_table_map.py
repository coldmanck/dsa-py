from .map import MapBase


class SortedTableMap(MapBase):
    def _find_index(self, k, low, high):
        if high < low:
            return high + 1
        else:
            mid = (high + low) // 2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return _find_index(k, low, mid - 1)
            else:
                return _find_index(k, mid + 1, high)

    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        idx = self._find_index(k, 0, len(self._table) - 1)
        if idx == len(self._table) or self._table[idx]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[idx]._value

    def __setitem__(self, k, v):
        idx = self._find_index(k, 0, len(self._table) - 1)
        if idx < len(self._table) and self._table[idx]._key == k:
            self._table[idx]._value = v
        else:
            self._table.insert(idx, self._Item(k, v))

    def __delitem__(self, k):
        idx = self._find_index(k, 0, len(self._table) - 1)
        if idx == len(self._table) or self._table[idx]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(idx)

    def __iter__(self):
        for item in self._table:
            yield item._key

    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        if len(self._table) > 0:
            return self._table[0]._key, self._table[0]._value
        else:
            return None

    def find_max(self):
        if len(self._table) > 0:
            return self._table[-1]._key, self._table[-1]._value
        else:
            return None

    def find_ge(self, k):
        idx = self._find_index(k, 0, len(self._table) - 1)
        if idx < len(self._table):
            return self._table[idx]._key, self._table[idx]._value
        else:
            return None

    def find_lt(self, k):
        idx = self._find_index(k, 0, len(self._table) - 1)
        if idx > 0:
            return self._table[idx - 1]._key, self._table[idx - 1]._value
        else:
            return None

    def find_gt(self, k):
        idx = self._find_index(k, 0, len(self._table) - 1)
        if idx < len(self._table) - 1 and self._table[idx]._value == k:
            return self._table[idx + 1]._key, self._table[idx]._value
        else:
            return None

    def find_range(self, start=None, stop=None):
        """ Iterate all (key, value) pairs s.t. start <= key < stop. """

        if start is None:
            idx = 0
        else:
            idx = self._find_index(start, 0, len(self._table) - 1)

        while idx < len(self._table) and (stop is None or self._table[idx]._key < stop):
            yield self._table[idx]._key, self._table[idx]._value
            idx += 1
