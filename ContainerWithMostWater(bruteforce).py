


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                mini = min(heights[i], heights[j])
                max_water = mini * (j - i)
                maxi = max(maxi, max_water)
        return maxi
