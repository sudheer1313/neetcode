


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxi = 0
        for i in range(len(s)):
            s1 = ""
            for j in range(i, len(s)):
                s1 += s[j]
                if s1[::-1] == s1:
                    maxi = max(maxi, len(s))
                    if len(s1) > len(res):
                        res = s1
        return res


