


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        d = dict()
        for i in points:
            t = tuple(i)
            s = math.sqrt((t[0] * t[0]) + (t[1] * t[1]))
            d[t] = s
        d = dict(sorted(d.items(), key=lambda x: x[1]))
        a = 0
        l = []
        for i in d:
            if a == k:
                break
            a += 1
            l.append(list(i))
        return l





