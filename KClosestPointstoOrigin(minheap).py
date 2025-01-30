


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = []
        for i in points:
            t1, t2 = i
            s = math.sqrt((t1 * t1) + (t2 * t2))
            l.append([s, t1, t2])
        heapq.heapify(l)
        l1 = []
        for i in range(k):
            d, x, y = heapq.heappop(l)
            l1.append([x, y])
        return l1



