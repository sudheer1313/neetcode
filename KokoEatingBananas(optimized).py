import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        ans = r = max(piles)
        while l <= r:
            mid = (l + r) // 2
            s = 0
            for i in piles:
                g = math.ceil(i / mid)
                s += g
            if s <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans



