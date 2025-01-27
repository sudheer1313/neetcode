


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l = sorted(score, reverse=True)

        for i in range(len(score)):
            if score[i] == l[0]:
                score[i] = "Gold Medal"
            elif score[i] == l[1]:
                score[i] = "Silver Medal"
            elif score[i] == l[2]:
                score[i] = "Bronze Medal"
            else:
                score[i] = str(l.index(score[i]) + 1)
        return score

