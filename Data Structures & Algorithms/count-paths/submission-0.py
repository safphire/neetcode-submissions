class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n

        for i in range(m-1 , -1, -1):
            newRow = [0] * n
            newRow[n-1] = 1
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + prevRow[j]
            prevRow = newRow
        return prevRow[0]