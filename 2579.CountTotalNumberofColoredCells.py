


class Solution:
    def coloredCells(self, n: int) -> int:
        prev = 1
        for i in range(0, n):
            res = prev + (4 * i)
            prev = res
        return res


