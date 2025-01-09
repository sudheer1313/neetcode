

import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t in s:
            return t
        if len(s) < len(t):
            return ""
        res = sys.maxsize
        res1 = ""
        l = len(set(t))

        for i in range(len(s)):
            d = dict()
            s1 = ""
            count = 0
            for j in range(i, len(s)):
                s1 += s[j]
                if s[j] in t:
                    if s[j] in d:
                        d[s[j]] += 1
                    else:
                        d[s[j]] = 1
                    if d[s[j]] == t.count(s[j]):
                        count += 1
                if count == l:
                    if len(s1) < res:
                        res = len(s1)
                        res1 = s1
                    break
        return res1

