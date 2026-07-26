class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []


        for i, a in enumerate(words):
            for j, b in enumerate(words):
                if i != j:
                    if a in b:
                        if a not in res:
                            res.append(a)
        return res
                    