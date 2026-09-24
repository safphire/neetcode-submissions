class Solution:
    def countBits(self, n: int) -> List[int]:
        retval = [0] * (n + 1)
        for i in range(n + 1):
            ptr = i
            count = 0
            while i > 0:
                if i & 1 == 1:
                    count += 1
                i = i >> 1
            print(count)
            retval[ptr] = count
        return retval
