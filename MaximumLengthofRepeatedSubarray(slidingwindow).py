class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1 = dict()
        d2 = dict()
        l = 0
        li = []
        if len(p) > len(s):
            return []
        for i in p:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for i in range(len(p)):
            if s[i] in d2:
                d2[s[i]] += 1
            else:
                d2[s[i]] = 1
        if d1 == d2:
            li.append(0)
        for r in range(len(p), len(s)):
            d2[s[l]] -= 1
            if d2[s[l]] <= 0:
                d2.pop(s[l])
            l += 1
            if s[r] in d2:
                d2[s[r]] += 1
            else:
                d2[s[r]] = 1
            if d1 == d2:
                li.append(l)
        return li




