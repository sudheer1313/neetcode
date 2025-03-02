2570.MergeTwo2DArraysbySummingValues.py


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        d1 = {}
        for val in range(len(nums1)):
            val1, val2 = nums1[val]
            if val1 not in d1:
                d1[val1] = val2
            else:
                d1[val1] += val2

        for val in range(len(nums2)):
            val3, val4 = nums2[val]
            if val3 not in d1:
                d1[val3] = val4
            else:
                d1[val3] += val4
        d1 = dict(sorted(d1.items(), key=lambda x: x[0]))
        for k in d1:
            res.append([k, d1[k]])

        return res

