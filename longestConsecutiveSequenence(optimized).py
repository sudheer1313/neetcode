


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uni = set(nums)
        maxi = 0
        for i in uni:
            if i - 1 not in uni:
                c = 1
                while i + c in uni:
                    c += 1
                maxi = max(maxi, c)
        return maxi


