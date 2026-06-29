class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_string = ""
        
        for letter in s:
            if letter.isalnum():
                stripped_string += letter.lower()
        
        i, j = 0, len(stripped_string) - 1

        while i < j:
            if stripped_string[i] != stripped_string[j]:
                return False
            i += 1
            j -= 1
        
        return True
