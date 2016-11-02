# Author: Alexandre Brilhante

''' Priority queue using insertion sort. '''

class PriorityQueue:
    def __init__(self, n):
        self._data = [0]*n
        self._n = n
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def add(self, value):
        if len(self) < self._n:
            self.insertion_sort(value)
        elif value > self.min():
            self.delete_min()
            self.insertion_sort(value)

    def min(self):
        if self.is_empty():
            return None
        return self._data[0]

    def delete_min(self):
        if self.is_empty():
            return None
        temp = self.min()
        self._data[0] = None
        for i in range(1, len(self)):
            self._data[i - 1] = self._data[i]
        self._size -= 1
        return temp

    def insertion_sort(self, value):
        i = 0
        while value > self._data[i] and i < len(self):
            i += 1
        for j in range(len(self), i, -1):
            self._data[j] = self._data[j - 1]
        self._data[i] = value
        self._size += 1

    def show(self):
        if self.is_empty():
            return None
        return self._data
