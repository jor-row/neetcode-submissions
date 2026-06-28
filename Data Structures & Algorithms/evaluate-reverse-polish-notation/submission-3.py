class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "/", "*"]

        for token in tokens:
            if token not in ops:
                stack.append(token)
            else:
                match token:
                    case "+":
                        a = int(stack.pop())
                        b = int(stack.pop())
                        stack.append(b+a)
                    case "-":
                        a = int(stack.pop())
                        b = int(stack.pop())
                        stack.append(b-a)
                    case "/":
                        a = int(stack.pop())
                        b = int(stack.pop())
                        stack.append(int(b / a))
                    case "*":
                        a = int(stack.pop())
                        b = int(stack.pop())
                        stack.append(b*a)

        return int(stack[-1])