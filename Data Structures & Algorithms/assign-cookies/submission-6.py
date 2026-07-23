class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        child = 0
        cookie = 0
        i = 0

        s.sort()
        g.sort()

        while len(s) > 0 and i < len(g) and child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
                cookie += 1
                i = 0
            else:
                cookie += 1
                i += 1

        return child

        