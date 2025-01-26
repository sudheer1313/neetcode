


class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i >= n:
                if i == n:
                    return 1
                else:
                    return 0
            one = dfs(i + 1)
            two = dfs(i + 2)
            return one + two

        return dfs(0)
