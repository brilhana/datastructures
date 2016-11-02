# Author: Alexandre Brilhante

''' d-ary heap. '''

class HeadD:
    def __init__(self, n, p):
        self._data = [0]*n
        self._n = n
        self._p = p
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def parent(self, j):
        return (j-1) // self._p

    def child(self, i, j):
        return self._p * i + j

    def small(self, i):
        small = self.child(i, 1)
        next_child = 2
        candidate = self.child(i, next_child)
        while next_child <= self._p and candidate < len(self):
            if self._data[candidate] < self._data[small]:
                small = candidate
            next_child += 1
            candidate = self.child(i, next_child)
        return small

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
            self.delete_min()
            self._data[self._size] = value
            self._size += 1
            self.swim(self._size - 1)

    def delete_min(self):
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

    def sink(self, i):
        temp = self._data[i]
        while self.child(i, 1) < len(self):
            child = self.small(i)
            if self._data[child] < temp:
                self._data[i] = self._data[child]
            else:
                break;
            i = child
        self._data[i] = temp
