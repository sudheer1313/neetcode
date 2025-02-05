


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        res = []

        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return
            if cur_sum > target or i == len(nums):
                return
            backtrack(i + 1, cur_sum)
            sol.append(nums[i])
            backtrack(i, cur_sum + nums[i])
            sol.pop()

        backtrack(0, 0)
        return res



