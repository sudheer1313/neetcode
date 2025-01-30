


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        str1 = ''.join([chr(i) for i in nums1])
        str2 = ''.join([chr(j) for j in nums2])
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


