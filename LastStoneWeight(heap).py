


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            if s1 != s2:
                heapq.heappush(stones, s1 - s2)
        if stones:
            return -heapq.heappop(stones)
        else:
            return 0



