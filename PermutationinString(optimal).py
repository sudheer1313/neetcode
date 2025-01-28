


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d1 = dict()
        d2 = dict()
        for i in s1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for i in range(len(s1)):
            if s2[i] in d2:
                d2[s2[i]] += 1
            else:
                d2[s2[i]] = 1
        if d1 == d2:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            d2[s2[l]] -= 1
            if d2[s2[l]] <= 0:
                d2.pop(s2[l])
            l += 1
            if s2[r] in d2:
                d2[s2[r]] += 1
            else:
                d2[s2[r]] = 1
            if d1 == d2:
                return True
        return False





