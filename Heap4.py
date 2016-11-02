# Author: Alexandre Brilhante

''' 4-ary heap. '''

class Heap4:
    def __init__(self, n):
        self._data = [0]*n
        self._n = n
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def parent(self, j):
        return (j-1) // 4

    def first_child(self, j):
        return 4*j + 1

    def has_first_child(self, j):
        return self.first_child(j) < len(self)

    def second_child(self, j):
        return 4*j + 2

    def has_second_child(self, j):
        return self.second_child(j) < len(self)

    def third_child(self, j):
        return 4*j + 3

    def has_third_child(self, j):
        return self.third_child(j) < len(self)

    def fourth_child(self, j):
        return 4*j + 4

    def has_fourth_child(self, j):
        return self.fourth_child(j) < len(self)

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

    def sink(self, j):
        if self.has_first_child(j):
            first = self.first_child(j)
            small = first
            if self.has_second_child(j):
                second = self.second_child(j)
                if self._data[second] < self._data[small]:
                    small = second
                if self.has_third_child(j):
                    third = self.third_child(j)
                    if self._data[third] < self._data[small]:
                        small = third
                    if self.has_fourth_child(j):
                        fourth = self.fourth_child(j)
                        if self._data[fourth] < self._data[small]:
                            small = fourth
            if self._data[small] < self._data[j]:
                self._data[j], self._data[small] = self._data[small], self._data[j]
                self.sink(small)
