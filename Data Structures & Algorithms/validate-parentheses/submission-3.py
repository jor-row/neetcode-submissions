class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        print(brackets.values())

        for b in s:
            if b in brackets.values():
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                    
                if stack.pop() != brackets[b]:
                    return False

        if len(stack) == 0:
            return True

        return False


        