class MinStack:

    def __init__(self):
        self.min_stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if len(self.mins) == 0 or val <= self.mins[-1]:
            self.mins.append(val)
        

    def pop(self) -> None:
        removed = self.min_stack.pop()
        if len(self.mins) > 0 and removed == self.mins[-1]:
            self.mins.pop()
        
    def top(self) -> int:
        return self.min_stack[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
