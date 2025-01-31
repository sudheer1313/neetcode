


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        l = 0
        maxi = 0
        s1 = "".join([chr(i) for i in nums1])
        s2 = "".join([chr(i) for i in nums2])
        s = ""
        for r in range(len(s1)):
            s += s1[r]
            while s not in s2:
                l += 1
                s = s1[l:r + 1]
            maxi = max(maxi, len(s))
        return maxi





