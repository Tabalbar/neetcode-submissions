class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        num_islands = 0

        def dfs(i,j):
            if i >= ROWS or j >= COLS or i < 0 or j < 0 or grid[i][j] == "0" or (i,j) in visited:
                return

            visited.add((i,j))

            for di, dj in dirs:
                new_i, new_j = i + di, j + dj
                dfs(new_i, new_j)

            

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    num_islands += 1

        return num_islands