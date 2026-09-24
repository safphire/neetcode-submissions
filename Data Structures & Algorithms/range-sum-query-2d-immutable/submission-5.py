class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.rowsum = [[0] * self.n for i in range(self.m)]
        # print(len(matrix))
        for i in range (self.m):
            currSum = 0
            for j in range(self.n):
                currSum += matrix[i][j]
                self.rowsum[i][j] = currSum

        # for i in range(len(matrix)):
        #     print(self.rowsum[i])    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        finalsum = 0
        for i in range (row1, row2 + 1):
            print(finalsum)
            finalsum += (self.rowsum[i][col2] - (self.rowsum[i][col1-1] if col1 > 0 else 0))
        return finalsum

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)