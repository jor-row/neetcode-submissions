class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # convert them to dictionaries and compare

        s_dict = {}
        t_dict = {}

        for a in s:
            if a in s_dict.keys():
                s_dict[a] += 1
            else: 
                s_dict[a] = 0

        for a in t:
            if a in t_dict.keys():
                t_dict[a] += 1
            else: 
                t_dict[a] = 0

        return s_dict == t_dict