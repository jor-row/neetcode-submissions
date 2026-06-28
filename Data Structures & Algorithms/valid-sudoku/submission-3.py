class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {} # a hash map of sets
        cols = {}
        squares = {}

        for r in range(9):
            rows[r] = {}
            for c in range(9):
                if c not in cols:
                    cols[c] = {}

                if (r // 3, c // 3) not in squares:
                    squares[(r // 3, c // 3)] = {}

                num = board[r][c]

                if num != ".":

                    if num in rows[r]:
                        print("1, ", num, r)
                        return False
                    else:
                        rows[r][num] = 1

                    if num in cols[c]:
                        print("2")
                        return False
                    else:
                        cols[c][num] = 1
                    
                    if num in squares[(r // 3, c // 3)]: 
                        print("3")
                        return False
                    else:
                        squares[(r // 3, c // 3)][num] = 1

        return True

                    
        