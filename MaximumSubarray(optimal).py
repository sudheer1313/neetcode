


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -sys.maxsize - 1
        s = 0
        for i in nums:
            s += i
            maxi = max(maxi, s)
            if s < 0:
                s = 0

        return maxi


