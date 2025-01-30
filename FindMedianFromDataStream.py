


class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        self.l.append(num)
        self.l.sort()

    def findMedian(self) -> float:
        z = len(self.l)
        if z == 1:
            return float(self.l[0])
        if z % 2 == 0:
            ans = (self.l[z // 2] + self.l[(z // 2) - 1]) / 2
        else:
            ans = self.l[z // 2]
        return ans




