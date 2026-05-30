class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_length = len(board)
        col_length = len(board[0])

        for row in range(row_length):
            num_freq = {}
            for col in range(col_length):
                num = board[row][col]
                if num in num_freq and num != ".":
                    return False
                else:
                    num_freq[num] = 1

        for row in range(row_length):
            num_freq = {}
            for col in range(col_length):
                num = board[col][row]
                if num in num_freq and num != ".":
                    print(row, col)
                    return False
                else:
                    num_freq[num] = 1
        
        def check_square(starting_i, starting_j):
            num_freq = {}
            for i in range(starting_i, starting_i + 3):
                for j in range(starting_j, starting_j + 3):
                    num = board[i][j]
                    if num in num_freq and num != ".":
                        return False
                    else:
                        num_freq[num] = 1
            return True
        
        starting_rows = [0,3,6]
        starting_cols = [0,3,6]

        for row in starting_rows:
            for col in starting_cols:
                if not check_square(row, col):
                    return False

        return True



