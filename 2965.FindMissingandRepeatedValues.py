


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l = []
        for i in grid:
            for j in i:
                l.append(j)
        c = Counter(l)
        for i in c:
            if c[i] > 1:
                dup = i
                break
        n = len(l)
        miss_val = n * (n + 1) / 2 - sum(set(l))
        return [dup, int(miss_val)]




