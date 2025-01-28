

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        c = 0
        for i in range(len(nums)):
            s = 1
            for j in range(i, len(nums)):
                s *= nums[j]
                if s < k:
                    c += 1
                if s >= k:
                    break
        return c

