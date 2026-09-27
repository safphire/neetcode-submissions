import copy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        column = len(matrix[0])
        rows, cols = [False] * row, [False] * column

        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        
        for r in range(row):
            for c in range(column):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0
        # print(copyMat)
            
        