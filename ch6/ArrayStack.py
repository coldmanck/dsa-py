class EmptyException(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        if self.is_empty():
            return EmptyException('Stack is empty!')
        else:
            return str(self._data)

    def is_empty(self):
        return self.__len__() == 0

    def push(self, x):
        self._data.append(x)

    def top(self):
        if self.is_empty():
            return EmptyException('Stack is empty!')
        else:
            return self._data[-1]

    def pop(self):
        if self.is_empty():
            return EmptyException('Stack is empty!')
        else:
            return self._data.pop()

    def print(self):
        if self.is_empty():
            return EmptyException('Stack is empty!')
        else:
            return str(self._data)
