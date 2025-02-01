


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l = []
        for i in range(len(s)):
            res = sys.maxsize
            for j in range(0, len(s)):
                if s[j] == c:
                    r = abs(i - j)
                    if r < res:
                        res = r
            l.append(res)
        return l


