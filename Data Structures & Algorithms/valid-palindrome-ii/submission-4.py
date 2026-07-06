class Solution:
    def validPalindrome(self, s: str, canDel: bool = True) -> bool:
        l = 0
        r = len(s) - 1
        already_deleted = False

        while l < r:
            if s[l] != s[r]:
                if already_deleted or canDel == False:
                    return False
                else:
                    already_deleted = True
                    return self.validPalindrome(s[:r]+s[r+1:], False) or self.validPalindrome(s[:l]+s[l+1:], False)
            else:
                l += 1
                r -= 1
        
        return True
        
        