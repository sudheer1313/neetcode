


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = -sys.maxsize - 1
        for i in range(len(s)):
            s1 = ""
            for j in range(i, len(s)):
                s1 += s[j]
                if s1 == s1[::-1]:
                    if len(s1) > res:
                        res = len(s1)
                        result = s1
        return result



