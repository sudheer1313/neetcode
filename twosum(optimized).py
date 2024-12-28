class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hashmap(optimized)
        d = dict()
        for i, val in enumerate(nums):
            if target - val in d:
                return [d[target - val], i]

            d[val] = i

