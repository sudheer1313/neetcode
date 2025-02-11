


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            k = 0
            c = 0
            for j in range(i, len(needle) + i):
                if haystack[j] == needle[k]:
                    c += 1
                k += 1
            if c == len(needle):
                return i
        return -1
