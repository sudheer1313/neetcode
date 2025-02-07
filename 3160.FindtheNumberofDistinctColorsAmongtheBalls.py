


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        d = dict()
        res = []
        for b_c in queries:
            ball = b_c[0]
            color = b_c[1]
            d[ball] = color
            l = len(set(d.values()))
            res.append(l)
        return res


