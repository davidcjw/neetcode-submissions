class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [-1] * self.capacity
        self.size = 0

    def get(self, i: int) -> int:
        # always in bounds
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # always in bounds
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        old_capacity = self.capacity
        self.capacity *= 2
        self.arr += [-1] * old_capacity
    
    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
