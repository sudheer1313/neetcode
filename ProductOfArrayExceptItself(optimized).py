ProductOfArrayExceptItself(optimized).py


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l = [0] * len(nums)
        r = [0] * len(nums)
        left = right = 1
        for i in range(len(nums)):
            l[i] = left
            left *= nums[i]
        for j in range(len(nums) - 1, -1, -1):
            r[j] = right
            right = right * nums[j]
        for k in range(len(res)):
            res[k] = l[k] * r[k]
        return res



