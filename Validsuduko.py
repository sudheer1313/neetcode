class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def sub_check(row1, row2, col1, col2):
            seen = set()
            for i in range(row1, row2 + 1):
                for j in range(col1, col2 + 1):
                    if board[i][j] in seen and board[i][j] != ".":
                        return False
                    seen.add(board[i][j])
            return True

        p1 = sub_check(0, 2, 0, 2)
        p2 = sub_check(0, 2, 3, 5)
        p3 = sub_check(0, 2, 6, 8)
        p4 = sub_check(3, 5, 0, 2)
        p5 = sub_check(3, 5, 3, 5)
        p6 = sub_check(3, 5, 6, 8)
        p7 = sub_check(6, 8, 0, 2)
        p8 = sub_check(6, 8, 3, 5)
        p9 = sub_check(6, 8, 6, 8)

        def check(matrix):
            c = len(matrix[0])
            for i in range(len(matrix)):
                uni = set()
                for j in range(c):
                    if matrix[i][j] in uni and matrix[i][j] != ".":
                        return False
                    uni.add(matrix[i][j])
            return True

        transpose = [[0] * len(i) for i in board]
        col = len(board[0])
        for i in range(len(board)):
            for j in range(col):
                transpose[j][i] = board[i][j]
        row_check = check(board)
        col_check = check(transpose)
        return row_check and col_check and p1 and p2 and p3 and p4 and p5 and p6 and p7 and p8 and p9




