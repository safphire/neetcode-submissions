import copy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        column = len(matrix[0])
        def propagateZero(matrix, i, j, row, column):
            for c in range(column):
                matrix[i][c] = 0
            for r in range(row):
                matrix[r][j] = 0

        copyMat = copy.deepcopy(matrix)
        for i in range(row):
            for j in range(column):
                if copyMat[i][j] == 0:
                    propagateZero(matrix, i, j, row, column)
        # print(copyMat)
            
        