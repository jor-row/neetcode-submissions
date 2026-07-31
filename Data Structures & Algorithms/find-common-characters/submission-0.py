class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letters = Counter(words[0])
        

        for word in words:
            wl = Counter(word)

            for char in letters:
                if char not in wl:
                    letters[char] = 0
                elif letters[char] > wl[char]:
                    letters[char] = wl[char]
            
        res = []
        for char in letters:
            for i in range(letters[char]):
                res.append(char)
        return res

        