class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        ballCount = Counter("balloon")

        for i in range(int(len(text) / len("balloon"))):
            for char in ballCount:
                count[char] -= ballCount[char]
                print("testing char, ", char, count[char], ballCount[char])
                if count[char] < 0:
                    return i

        
        return int(len(text) / len("balloon"))