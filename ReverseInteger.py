


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        negative = x < 0
        x = abs(x)
        while x:
            d = x % 10
            result = result * 10 + d
            x //= 10
        if negative:
            result = -result

        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 0
        return result

