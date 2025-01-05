RotateImage.py


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        col = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(i + 1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            matrix[i] = reversed(matrix[i])




