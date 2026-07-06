class Solution:
    def romanToInt(self, s: str) -> int:
        s2v = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        stack = ["M","D","C","L","X","V","I"]

        arr = []

        for letter in s:
            arr.append(s2v[letter])

        print(arr)

        if len(arr) == 1:
            return arr[0]

        
        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                arr[i] -= arr[i-1]
                arr[i-1] = 0

        res = 0

        for num in arr:
            res += num

        return res

        
        