


class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(0, n + 1):
            num = i
            ans = 0
            while num != 0:
                num = num & (num - 1)
                ans += 1
            l.append(ans)
        return l


