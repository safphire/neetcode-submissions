class Solution:
    def climbStairs(self, n: int) -> int:

        def climb(step, cache):
            if step in cache:
                return cache[step]
            if step == 0:
                return 1
            if step < 0:
                return 0
            
            ways = climb(step - 1, cache) + climb(step - 2, cache)
            cache[step] = ways
            return cache[step]
        
        return climb(n, {})
        