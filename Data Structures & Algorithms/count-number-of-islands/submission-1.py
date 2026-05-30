class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        
        visited = set()
        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            
            while len(q) > 0:
                cr, cl = q.pop()
                directions = [[1,0], [0,1], [-1,0],[0,-1]]
                for dirR, dirC in directions:
                    curr_r = dirR + cr
                    curr_c = dirC + cl
                    if curr_r in range(rows) and curr_c in range(cols) and grid[curr_r][curr_c] == "1" and (curr_r,curr_c) not in visited:
                        q.append((curr_r, curr_c))
                        visited.add((curr_r, curr_c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    num_islands += 1
        return num_islands