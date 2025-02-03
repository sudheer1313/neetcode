


class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        l = 32 - len(n)
        s = "0" * l + n
        s = s[::-1]
        return int(s, 2)

