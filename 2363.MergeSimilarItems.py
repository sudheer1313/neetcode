


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = {}
        for val, wei in items1:
            if val not in d:
                d[val] = wei
            else:
                d[val] += wei
        for val, wei in items2:
            if val not in d:
                d[val] = wei
            else:
                d[val] += wei
        d = dict(sorted(d.items(), key=lambda x: x[0]))
        res = []
        for k in d:
            res.append([k, d[k]])
        return res



