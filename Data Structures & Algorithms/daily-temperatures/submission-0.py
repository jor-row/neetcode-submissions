class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0 for i in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx
            
            stack.append(i)

        


        return result
                
        