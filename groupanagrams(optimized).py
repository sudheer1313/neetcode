class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for i in strs:
            s="".join(sorted(i))
            if s  in d:
                d[s].append(i)
            else:
                d[s]=[i]
        l=[]
        for i in d:
            l.append(d[i])
        return l