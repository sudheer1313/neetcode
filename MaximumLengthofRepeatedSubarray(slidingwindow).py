


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        str1 = "".join(map(str, nums1))
        str2 = "".join(map(str, nums2))
        maxi = 0
        for i in range(len(str1)):
            s = ""
            for j in range(i, len(str1)):
                s += str1[j]
                if s in str2:
                    maxi = max(maxi, len(s))
                else:
                    break
        return maxi


