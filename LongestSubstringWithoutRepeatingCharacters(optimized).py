


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uni = set()
        right = left = maxi = 0
        for right in range(len(s)):
            while s[right] in uni:
                uni.remove(s[left])
                left += 1
            else:
                uni.add(s[right])
            maxi = max(maxi, len(uni))
        return maxi






