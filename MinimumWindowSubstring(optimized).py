

import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d2 = dict()
        for i in t:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
        l = 0
        count = 0
        d1 = dict()
        res = sys.maxsize
        res_str = ""
        for r in range(len(s)):
            if s[r] in d1:
                d1[s[r]] += 1
            else:
                d1[s[r]] = 1
            if s[r] in d2 and d1[s[r]] == d2[s[r]]:
                count += 1
            while count == len(d2):
                if r - l + 1 < res:
                    res_str = ""
                    res = r - l + 1
                    res_str = s[l:r + 1]
                d1[s[l]] -= 1
                if s[l] in d2 and d1[s[l]] < d2[s[l]]:
                    count -= 1
                l += 1
        return res_str






