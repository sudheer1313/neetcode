

import sys


class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = sys.maxsize
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            mini = min(mini, nums[mid])
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        return mini




