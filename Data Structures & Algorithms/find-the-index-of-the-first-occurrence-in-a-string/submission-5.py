class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] != needle[0]:
                continue
            j = i
            k = 0
            while k < len(needle) and haystack[j] == needle[k]:
                j += 1
                k += 1
            if k == len(needle):
                return i
            
        return -1
        