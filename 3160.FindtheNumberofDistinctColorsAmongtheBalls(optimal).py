


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = {}
        res = []
        for b_c in queries:
            ball = b_c[0]
            color = b_c[1]
            if ball in balls:
                c = balls[ball]
                colors[c] -= 1
                if colors[c] <= 0:
                    del colors[c]
            balls[ball] = color
            if color in colors:
                colors[color] += 1
            else:
                colors[color] = 1
            res.append(len(colors))
        return res

