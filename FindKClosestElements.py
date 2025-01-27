


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        d = list()
        for i in arr:
            ans = abs(i - x)
            d.append((i, ans))
        d = sorted(d, key=lambda x: x[1])
        a = 0
        l = []
        for i in d:
            if a == k:
                break
            l.append(i[0])
            a += 1
        return sorted(l)



