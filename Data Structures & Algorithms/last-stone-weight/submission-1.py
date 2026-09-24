class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def maxHeap(stones):
            self.heap = [None]
            for i in stones:
                heapPush(i)
        
        def heapPush(val):
            self.heap.append(val)
            i = len(self.heap) - 1
            while i // 2 > 0:
                if self.heap[i // 2] < self.heap[i]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[i // 2]
                    self.heap[i // 2] = temp
                    i = i // 2
                else:
                    break

        def heapPop():
            if len(self.heap) <= 1:
                return 0

            ret = self.heap[1]
            last = self.heap.pop()
            
            if len(self.heap) > 1:
                self.heap[1] = last
                i = 1
                while i * 2 < len(self.heap):
                    child = i * 2
                    if child + 1 < len(self.heap) and self.heap[child] < self.heap[child + 1]:
                        child += 1
                    
                    if self.heap[child] > self.heap[i]:
                        temp = self.heap[child]
                        self.heap[child] = self.heap[i]
                        self.heap[i] = temp
                        i = child
                    else:
                        break
            return ret

        maxHeap(stones)
        while len(self.heap) > 2:
            first = heapPop()
            second = heapPop()
            # print (f'{first} - {second} = {abs(first - second)}')
            if first != second:
                first = abs(first - second)
                heapPush(first)
        
        heapPush(0)
        return self.heap[1]
    
        # for stone in stones:
        #     if self.comp > 2:


        