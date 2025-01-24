


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        sub_list = []

        def backtrack(i):
            if i >= len(nums):
                result.append(sub_list[:])
                return
            sub_list.append(nums[i])
            backtrack(i + 1)
            sub_list.pop()
            backtrack(i + 1)

        backtrack(0)
        return result


