

class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(0, n + 1):
            s = bin(i)[2:]
            l.append(s.count("1"))
        return l


