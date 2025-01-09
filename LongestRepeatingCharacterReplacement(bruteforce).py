


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            d = {}
            maxi = 0
            for j in range(i, len(s)):
                if s[j] in d:
                    d[s[j]] += 1
                else:
                    d[s[j]] = 1
                maxi = max(maxi, d[s[j]])
                if j - i + 1 - maxi <= k:
                    res = max(res, j - i + 1)
        return res

