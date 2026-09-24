class DynamicArray:

    def __init__(self, capacity: int):
        self.length = 0
        self.capacity = capacity
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # if self.length == self.capacity:
        #     self.resize()
        # for j in range(i+1, len(self.arr)):
        #     self.arr[j] = self.arr[j-1]
        self.arr[i] = n
        # self.length += 1

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            val = self.arr[self.length-1]
            self.arr[self.length-1] = 0
            self.length -= 1
        return val

    def resize(self) -> None:
        self.capacity *= 2
        temparr = [0] * self.capacity
        for i in range(self.length):
            temparr[i] = self.arr[i]
        self.arr = temparr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity