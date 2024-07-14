import _ctypes
a = 17
id_a = id(15)

print(_ctypes.PyObj_FromPtr(id_a))


class PointerArray:
    def __init__(self):
        self.size = 0
        self.array = []

    def __len__(self):
        return self.size

    def __getitem__(self, index: int):
        if not 0 <= index < self.size:
            raise IndexError("index out of range")
        return self.array[index]

    def append(self, value: any):
        self.array.append(id(value))
        self.size += 1

    @staticmethod
    def get_value_by_id(id: int) -> any:
        return _ctypes.PyObj_FromPtr(id)

    def __repr__(self) -> str:
        return f"{[PointerArray.get_value_by_id(self.array[i]) for i in range(self.size)]}"
