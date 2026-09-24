class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [None]
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        self.heap.append(val)
        
        start = len(self.heap) - 1
        while start // 2 > 0:
            if self.heap[start // 2] > self.heap[start]:
                tmp = self.heap[start // 2]
                self.heap[start // 2] = self.heap[start]
                self.heap[start] = tmp
            start = start // 2

        if len(self.heap) > self.k + 1:
            self.heap[1] = self.heap.pop()
            i = 1

            #percolate down
            while 2 * i < len(self.heap):
                if (2 * i + 1) < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[2 * i + 1] < self.heap[i]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[i * 2 + 1]
                    self.heap[i * 2 + 1] = temp
                    i = i * 2 + 1
                elif self.heap[i] > self.heap[2 * i]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[i * 2]
                    self.heap[i * 2] = temp
                    i = i * 2
                else:
                    break
        return self.heap[1]
        

