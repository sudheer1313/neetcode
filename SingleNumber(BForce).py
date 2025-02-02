
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            f = True
            for j in range(len(nums)):
                if nums[i] == nums[j] and i != j:
                    f = False
                    break
            if f:
                return nums[i]


