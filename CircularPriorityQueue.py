# Author: Alexandre Brilhante

''' Circular priority queue. '''

class CircularPriorityQueue:
    def __init__(self, n):
        self._data = [0]*n
        self._n = n
        self._size = 0
        self._front = 0

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
        return self._data[self._front]

    def delete_min(self):
        temp = self.min()
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self)
        self._size -= 1
        return temp

    def insertion_sort(self, value):
        if self.is_empty():
            self._data[self._front] = value
            self._size += 1
        else:
            i = 0
            while value > self._data[(self._front + i) % self._n] and i < len(self):
                i += 1
                if i == len(self):
                    break
            start = (len(self) + self._front) % self._n
            stop = (self._front + i) % self._n
            if start < stop:
                for j in range(start, 0, -1):
                    self._data[j] = self._data[(j - 1)]
                self._data[0] = self._data[len(self)]
                for j in range(len(self), stop, -1):
                    self._data[j] = self._data[(j - 1)]
            else:
                for j in range(start, stop, -1):
                    self._data[j] = self._data[(j - 1)]
            self._data[(self._front + i) % self._n] = value
            self._size += 1

    def show(self):
        if self.is_empty():
            return None
        return self._data
