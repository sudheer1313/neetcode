


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col = len(matrix[0])
        row_uni = set()
        col_uni = set()
        for i in range(len(matrix)):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_uni.add(i)
                    col_uni.add(j)
        for i in row_uni:
            for j in range(col):
                matrix[i][j] = 0
        for i in col_uni:
            for j in range(len(matrix)):
                matrix[j][i] = 0



