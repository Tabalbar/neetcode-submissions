class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        num_islands = 0
        def dfs(r,c):
            if  (((r,c) in visited) or (r >= rows or r < 0 or c >= cols or c < 0) or (grid[r][c] == "0")):
                return
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    num_islands +=1

        return num_islands