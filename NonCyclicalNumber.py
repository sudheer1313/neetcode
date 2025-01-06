

class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate(n):
            sm = sum(int(digit) ** 2 for digit in str(n))
            return sm

        uni = set()
        while n != 1 and n not in uni:
            uni.add(n)
            n = calculate(str(n))
        return n == 1




