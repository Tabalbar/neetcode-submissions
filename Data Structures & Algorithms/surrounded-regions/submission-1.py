class Solution:
    def solve(self, board: List[List[str]]) -> None:
        connectedToOuterEdge = {}
        rows = len(board)
        cols = len(board[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(r,c):
            val = board[r][c]
            if val == "O":
                connectedToOuterEdge[(r,c)] = 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and (nr,nc) not in connectedToOuterEdge:
                        dfs(r + dr, c + dc)
                


        for c in range(cols):
            dfs(0,c)
        for c in range(cols):
            dfs(rows-1,c)
        for r in range(rows):
            dfs(r,0)
        for r in range(rows):
            dfs(r, cols-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in connectedToOuterEdge:
                    board[r][c] = "X"
