

from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = permutations(nums)
        l = []
        for i in n:
            l.append(list(i))
        return l



