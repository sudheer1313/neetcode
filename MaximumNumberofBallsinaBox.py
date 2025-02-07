


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = dict()
        for i in range(lowLimit, highLimit + 1):
            l = list(str(i))
            s = 0
            for i in l:
                s += int(i)
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        for i in d:
            return d[i]

