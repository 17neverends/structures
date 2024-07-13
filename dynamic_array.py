import ctypes


class DynamicArray:
    def __init__(self, initial_capacity=1):
        self.size = 0
        self.capacity = initial_capacity
        self.array = (ctypes.py_object * self.capacity)()

    def __len__(self):
        return self.size

    def __getitem__(self, index: int):
        if not 0 <= index < self.size:
            raise IndexError("index out of range")
        return self.array[index]

    def append(self, value: any):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = value
        self.size += 1

    def insert(self, index: int, value: any):
        if not 0 <= index <= self.size:
            raise IndexError("index out of range")
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise "array size is 0"
        self.array[self.size - 1] = 0
        self.size -= 1

    def remove(self, index: int):
        if not 0 <= index < self.size:
            raise IndexError("index out of range")

        if index == self.size - 1:
            self.array[index] = 0
            self.size -= 1
            return

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = 0
        self.n -= 1

    def _resize(self, new_capacity: int):
        new_array = (ctypes.py_object * new_capacity)()
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __repr__(self):
        return f"{[self.array[i] for i in range(self.size)]}"
