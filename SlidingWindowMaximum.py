


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = []
        for i in range(len(nums) - k + 1):
            maxi = float("-inf")
            for j in range(i, k + i):
                maxi = max(maxi, nums[j])
            l.append(maxi)
        return l


