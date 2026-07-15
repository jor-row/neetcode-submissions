class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        indices = {}

        for i, char in enumerate(s):
            if char not in indices:
                indices[char] = [i]
            elif len(indices[char]) == 2:
                indices[char].pop()
                indices[char].append(i)
            else:
                indices[char].append(i)

        lss = -1

        for char in indices:
            if len(indices[char]) == 2:
                lss = max(lss, indices[char][1] - indices[char][0] - 1)

        return lss
        