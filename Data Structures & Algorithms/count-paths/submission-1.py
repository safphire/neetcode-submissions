class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def findPath(r: int, c: int, cache):
            if r == m or c == n:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == m - 1 and c == n - 1:
                return 1
            
            cache[r][c] = findPath(r + 1, c, cache) + findPath(r, c +1, cache)
            return cache[r][c]
        
        return findPath(0, 0, [[0] * n for i in range (m)])