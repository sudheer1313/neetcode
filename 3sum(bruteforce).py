3sum(bruteforce).py



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        uni = set()
        res = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        r = sorted([nums[i], nums[j], nums[k]])
                        if tuple(r) not in uni:
                            uni.add(tuple(r))
                            res.append(r)
        return res

