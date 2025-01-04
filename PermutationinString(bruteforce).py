


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(s1))
        for i in range(len(s2)):
            s = ""
            s += s2[i]
            p1 = "".join(sorted(s))
            if s1 == p1:
                return True
            for j in range(i + 1, len(s2)):
                s += s2[j]
                p = "".join(sorted(s))
                if s1 == p:
                    return True

        return False



