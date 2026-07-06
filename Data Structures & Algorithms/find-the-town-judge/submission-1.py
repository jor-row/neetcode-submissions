class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hash_map = {}
        hash_map_reverse = {}


        for [a, b] in trust:
            if a not in hash_map:
                hash_map[a] = [b]
            else:
                hash_map[a].append(b)


            if b not in hash_map_reverse:
                hash_map_reverse[b] = [a]
            else:
                hash_map_reverse[b].append(a)

            

        people = hash_map.keys()

        for key in hash_map_reverse:
            if hash_map_reverse[key] == list(people):
                return key

        return -1
        