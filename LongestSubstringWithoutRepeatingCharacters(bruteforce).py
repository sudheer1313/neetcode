

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        for i in range(len(s)):
            uni = set()
            uni.add(s[i])
            for j in range(i + 1, len(s)):
                if s[j] not in uni:
                    uni.add(s[j])
                else:
                    break
            maxi = max(maxi, len(uni))
        return maxi
