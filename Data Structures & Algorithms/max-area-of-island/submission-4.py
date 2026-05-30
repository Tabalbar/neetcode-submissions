class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        visited = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0 or (i,j) in visited:
                return 0
            visited.add((i,j))
            return (1 + dfs(i + 1, j) + 
                        dfs(i, j + 1) +
                        dfs(i - 1, j) +
                        dfs(i, j - 1))
            


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    if area > max_area:
                        max_area = area

        return max_area