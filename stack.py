class Stack:
    def __init__(self):
        self.items = []
        self.current_max = None
        self.current_min = None

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

        if self.current_max is None or item > self.current_max:
            self.current_max = item
        if self.current_min is None or item < self.current_min:
            self.current_min = item

    def pop(self):
        if self.is_empty():
            raise IndexError("stack size is 0")

        item = self.items.pop()

        if item == self.current_max or item == self.current_min:
            if self.is_empty():
                self.current_max = None
                self.current_min = None
            else:
                self.current_max = max(self.items)
                self.current_min = min(self.items)

        return item

    def get_last(self):
        if self.is_empty():
            raise IndexError("stack size is 0")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if self.is_empty():
            raise IndexError("stack size is 0")
        return self.current_max

    def get_min(self):
        if self.is_empty():
            raise IndexError("stack size is 0")
        return self.current_min

    def __repr__(self):
        return str(self.items)
