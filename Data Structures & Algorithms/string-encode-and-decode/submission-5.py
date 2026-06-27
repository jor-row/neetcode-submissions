class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for string in strs:
            encoded_string += f'{len(string)}#{string}'

        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        
        i = 0
        j = 0
        strings = []
        

        while i < len(s):
            if s[i] == '#' and s[j:i].isnumeric():
                curr_len = int(s[j:i])
                strings.append(s[i + 1: i + curr_len + 1])
                i += curr_len + 1
                j = i
            else:
                i += 1

        return strings

