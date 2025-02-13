


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c = 0
        while len(nums) >= 2:
            a = 0
            for i in nums:
                if i >= k:
                    a += 1
            if a == len(nums):
                return c
            nums = sorted(nums, reverse=True)
            e1 = nums.pop()
            e2 = nums.pop()
            ans = min(e1, e2) * 2 + max(e1, e2)
            nums.append(ans)
            c += 1
        return c


