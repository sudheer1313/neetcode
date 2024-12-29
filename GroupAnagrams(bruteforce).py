from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hashmap(dict1):
            c = Counter(dict1)
            return c

        def anagram(str1, str2):
            if len(str1) != len(str2):
                return False
            d1 = hashmap(str1)
            d2 = hashmap(str2)
            for i in d1:
                if i not in d2 or d1[i] != d2[i]:
                    return False
            return True

        uni = set()
        l1 = []
        for i in range(len(strs)):
            if strs[i] not in uni:
                l2 = [strs[i]]
                for j in range(i + 1, len(strs)):
                    if anagram(strs[i], strs[j]):
                        l2.append(strs[j])
                        uni.add(strs[j])
                l1.append(l2)
        return l1







