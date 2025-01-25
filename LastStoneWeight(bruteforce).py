


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            s1 = stones.pop()
            s2 = stones.pop()
            if s1 != s2:
                diff = abs(s1 - s2)
                stones.append(diff)
                stones.sort()
        if stones:
            return stones[0]
        else:
            return 0

