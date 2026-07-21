class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0

        for word in words:
            has_pref = True
            for i in range(len(pref)):
                if pref[i] != word[i]:
                    has_pref = False
                    break
            if has_pref:
                c += 1
        return c
        