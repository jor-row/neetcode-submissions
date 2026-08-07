class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(str1, str2):
            if len(str1) > len(str2):
                return False

            print(str2[:len(str1)])
            print(str2[len(str2) - len(str1):])
            if str2[:len(str1)] == str1 and str2[len(str2) - len(str1):] == str1:
                return True

        res = 0

        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1

        return res