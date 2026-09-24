class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.prefixSum = [[0] * (self.n + 1) for i in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.prefixSum[i + 1][j + 1] = self.prefixSum[i][j + 1] + self.prefixSum[i + 1][j] - self.prefixSum[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixSum[row2 + 1][col2 + 1] - self.prefixSum[row1][col2 + 1] - self.prefixSum[row2 + 1][col1] + self.prefixSum[row1][col1]