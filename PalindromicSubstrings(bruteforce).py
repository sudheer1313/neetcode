

class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            s1 = ""
            for j in range(i, len(s)):
                s1 += s[j]
                if s1[::-1] == s1:
                    c += 1
        return c
