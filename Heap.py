# Author: Alexandre Brilhante

''' Binary heap. '''

class Heap:
    def __init__(self, n):
        self._data = [0]*n
        self._n = n
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def parent(self, j):
        return (j-1) // 2

    def left(self, j):
        return 2*j + 1

    def has_left(self, j):
        return self.left(j) < len(self)

    def right(self, j):
        return 2*j + 2

    def has_right(self, j):
        return self.right(j) < len(self)

    def min(self):
        if self.is_empty():
            return None
        return self._data[0]

    def add(self, value):
        if self._size < self._n:
            self._data[self._size] = value
            self._size += 1
            self.swim(self._size - 1)
        elif value > self.min():
            self.suivant()
            self._data[self._size] = value
            self._size += 1
            self.swim(self._size - 1)

    def next(self):
        if self.is_empty():
            return None
        temp = self._data[0]
        self._data[0] = self._data[len(self) - 1]
        self._data[len(self) - 1] = None
        self._size -= 1
        if self.is_empty():
            return temp
        self.sink(0)
        return temp

    def show(self):
        if self.is_empty():
            return None
        return self._data

    def swim(self, j):
        parent = self.parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._data[j], self._data[parent] = self._data[parent], self._data[j]
            self.swim(parent)

    def sink(self, j):
        if self.has_left(j):
            left = self.left(j)
            small = left
            if self.has_right(j):
                right = self.right(j)
                if self._data[right] < self._data[left]:
                    small = right
            if self._data[small] < self._data[j]:
            	self._data[j], self._data[small] = self._data[small], self._data[j]
            	self.sink(small)
