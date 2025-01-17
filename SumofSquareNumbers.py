

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s = math.ceil(math.sqrt(c))
        l = 0
        r = s + 1
        while l <= r:
            a = (l * l) + (r * r)
            if a == c:
                return True
            elif a > c:
                r -= 1
            else:
                l += 1
        return False







