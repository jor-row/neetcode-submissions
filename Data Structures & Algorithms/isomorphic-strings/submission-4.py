class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_char2num = {}
        t_char2num = {}
        s_count = 1
        t_count = 1
        s_string = ""
        t_string = ""

        for i in range(len(s)):
            if s[i] not in s_char2num:
                s_char2num[s[i]] = str(s_count)
                s_count += 1
            if t[i] not in t_char2num:
                t_char2num[t[i]] = str(t_count)
                t_count += 1
            s_string += s_char2num[s[i]]
            t_string += t_char2num[t[i]]

        print(s_string)
        print(t_string)
        
        return s_string == t_string

            
        