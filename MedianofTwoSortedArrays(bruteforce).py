


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        s = sorted(nums3)
        l = len(s)
        if l % 2 == 0:
            return (s[(l // 2) - 1] + s[l // 2]) / 2
        else:
            return float(s[l // 2])




