


class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = 1
        for i in range(abs(n)):
            p *= x
        if n >= 0:
            return p
        else:
            return 1 / p



