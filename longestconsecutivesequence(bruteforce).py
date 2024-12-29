


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uni = list(set(nums))
        s = sorted(uni)
        maxi = 0
        for i in range(len(s)):
            c = 1
            for j in range(i + 1, len(s)):
                if s[i] + c == s[j]:
                    c += 1
            maxi = max(c, maxi)
        return maxi

