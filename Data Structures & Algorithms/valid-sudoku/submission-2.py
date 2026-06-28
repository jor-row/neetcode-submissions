class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we can check all rows
        # we can then check all columns
        # we can then check all squares

        # check the rows
        for row in board:
            row_dict = {}
            for num in row:
                if num == "." or num not in row_dict:
                    row_dict[num] = 1
                else: 
                    return False
            

        #now we want to do this for thw colums
        for col in range(9):
            column_dict = {}
            for row in range(9):
                if board[row][col] == "." or board[row][col] not in column_dict:
                    column_dict[board[row][col]] = 1
                else: 
                    return False

        # now we want to do this for the squares
        for a in [0, 3, 6]:
            for b in [0, 3, 6]:
                square_dict = {}
                # print("new square")
                for i in range(a, 3+a):
                    for j in range(b, 3+b):
                        # print("i, j", i, j, "is ", board[i][j])
                        if board[i][j] == "." or board[i][j] not in square_dict:
                            square_dict[board[i][j]] = 1
                        else: 
                            return False
        return True

                    
        