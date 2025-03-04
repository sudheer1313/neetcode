


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        c = 0
        for i in range(len(arr)):
            s = 0
            for j in range(i, len(arr)):
                s += arr[j]
                if s % 2 != 0:
                    c += 1
        return c
