class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows = [0] * rows
        zero_cols = [0] * cols
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows[i] = 1
                    zero_cols[j] = 1
        for i in range(rows):
            for j in range(cols):
                if zero_rows[i] == 1 or zero_cols[j] == 1:
                    matrix[i][j] = 0

        