class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        maxTime = 0


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c, 0))

        while len(queue) > 0:
            cr, cc, d = queue.popleft()
            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc
                if nr >= 0 and nc >= 0 and nr < rows and nc < cols:
                    if grid[nr][nc] == 1:
                        queue.append((nr,nc, d + 1))
                        maxTime = max(d + 1, maxTime)
                        grid[nr][nc] = 2

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        

        return maxTime

