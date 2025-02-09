


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (j - i) != nums[j] - nums[i]:
                    c += 1
        return c
