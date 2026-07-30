class Solution:
    def maxDepth(self, s: str) -> int:
        ob = "("
        cb = ")"
        stack = []
        max_depth = 0

        for char in s:
            if char == ob:
                stack.append(char)
            elif char == cb:
                max_depth = max(max_depth,len(stack))
                stack.pop()

        
        return max(max_depth,len(stack))