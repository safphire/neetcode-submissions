class Solution:
    def climbStairs(self, n: int) -> int:

        def climb(step, n, cache, ways):
            if step in cache:
                return cache[step]
            if step == n:
                return 1
            if step > n:
                return 0
            
            ways += climb(step + 1, n, cache, ways) + climb(step + 2, n, cache, ways)
            cache[step] = ways
            return cache[step]
        
        return climb(0, n, {}, 0)
        