class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        n = min(len(word1), len(word2))

        for i in range(n):
            s += word1[i]
            s += word2[i]


        if len(word2) > len(word1):
            for j in range(n, len(word2)):
                s += word2[j]
        else:
            for j in range(n, len(word1)):
                s += word1[j]

        return s

            