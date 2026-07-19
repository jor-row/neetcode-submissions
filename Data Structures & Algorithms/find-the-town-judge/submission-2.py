class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trusts = {}
        trusted = {}

        for rship in trust:
            a = rship[0]
            b = rship[1]
            # a trusts b

            if a not in trusts:
                trusts[a] = []
            trusts[a].append(b)

            if b not in trusted:
                trusted[b] = []
            trusted[b].append(a)

        
        
        trusts_nobody = []

        for i in range(1, n+1):
            if i not in trusts:
                trusts_nobody.append(i)

        if len(trusts_nobody) != 1:
            return -1

        for person in trusts_nobody:
            if len(trusted[person]) != n - 1:
                return -1

        return trusts_nobody[0]
