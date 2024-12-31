
class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=i+"sudheer"
        return s
    def decode(self, s: str) -> List[str]:
        s1=s.split('sudheer')
        return s1[:len(s1)-1]