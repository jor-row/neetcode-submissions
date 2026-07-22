class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            if log == "../":
                if len(stack):
                    stack.pop()
            elif log == "./":
                # do nothing
                print(stack)
            else:
                stack.append(log[:-1])

        print(stack)
        return len(stack)
        