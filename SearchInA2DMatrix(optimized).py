class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        new_list = []
        for i in nums:
            new_list += i
        l = 0
        r = len(new_list) - 1
        while l <= r:
            mid = (l + r) // 2
            if new_list[mid] == target:
                return True
            elif new_list[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
