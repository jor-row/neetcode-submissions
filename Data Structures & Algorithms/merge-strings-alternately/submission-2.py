class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        for i in range(min(len(word1), len(word2))):

            res += word1[i]
            res += word2[i]

        w = word1 if len(word1) > len(word2) else word2

        for j in range(min(len(word1), len(word2)), max(len(word1), len(word2))):

            res += w[j]


        return res

        