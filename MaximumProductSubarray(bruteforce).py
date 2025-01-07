

import sys


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = -sys.maxsize - 1
        for i in range(len(nums)):
            prod = nums[i]
            maxi = max(maxi, prod)
            for j in range(i + 1, len(nums)):
                prod *= nums[j]
                maxi = max(maxi, prod)
        return maxi



