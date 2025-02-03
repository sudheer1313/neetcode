class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) + 1):
            if i == len(nums):
                return i
            r = i | nums[i]
            if int(r) != i:
                return i
        # time complexity:o(nlogn)
        # space Complexity:o(1)
