class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        num_islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r, c))

            while len(q) > 0:
                curr_r, curr_c = q.popleft()
                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                for dir_r, dir_c in directions:
                    new_r, new_c = dir_r + curr_r, dir_c + curr_c
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == "1" and (new_r, new_c) not in visited:
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    bfs(row, col)
                    num_islands += 1

        return num_islands
