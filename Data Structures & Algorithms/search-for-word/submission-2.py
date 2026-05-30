class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, letter_index):
            if letter_index >= len(word):
                return True
             # Check boundaries
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            
            # If the current letter doesn't match, return False
            if board[i][j] != word[letter_index]:
                return False

            # Mark the cell as visited
            temp = board[i][j]
            board[i][j] = "#"

            # Explore all 4 directions
            neighbors = [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]
            for neighbor in neighbors:
                if dfs(neighbor[0], neighbor[1], letter_index + 1):
                    return True

            # Backtrack: unmark the cell
            board[i][j] = temp
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False