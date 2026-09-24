class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [1] * 2
        for i in range(1, n):
            val = cache[0] + cache[1]
            cache[0] = cache[1]
            cache[1] = val
        return cache[1]
