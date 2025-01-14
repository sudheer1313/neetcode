

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maxi=0
        res=0
        d=dict()
        for r in range(len(s)):
            if s[r] in d:
                d[s[r]]+=1
            else:
                d[s[r]]=1
            maxi=max(maxi,d[s[r]])
            while r-l+1-maxi>k:
                d[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
