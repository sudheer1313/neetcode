


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            l = height[i]
            r = height[i]
            k = 0
            while k < i:
                l = max(l, height[k])
                k += 1
            for j in range(i + 1, len(height)):
                r = max(r, height[j])
            ans += min(l, r) - height[i]
        return ans


