class Solution:
    def isValid(self, s: str) -> bool:

        o2c = {"(":")", "{":"}", "[":"]"}
        c2o = {")":"(", "}":"{", "]":"["}

        stack = []

        for bracket in s:
            print(stack)
            if stack and bracket in c2o:
                if stack[-1] != c2o[bracket]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(bracket)

        return True if len(stack) == 0 else False
        