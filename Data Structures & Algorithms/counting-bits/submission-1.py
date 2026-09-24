class Solution:
    def countBits(self, n: int) -> List[int]:
        retval = [0] * (n + 1)
        for i in range(1, n + 1):
            retval[i] = retval[i >> 1] + (i & 1)
        return retval