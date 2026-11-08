class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque([])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        # [1,2,3]
        # [1,2,3]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c,0))

        while len(queue) > 0:
            currr, currc, d = queue.popleft()
            for dr, dc in dirs:
                newr, newc = currr + dr, currc + dc
                if newr >= 0 and newc >= 0 and newr < rows and newc < cols:
                    val = grid[newr][newc]
                    if val == 0 or val == -1:
                        continue
                    else:
                        if grid[newr][newc] == 2147483647:
                            queue.append((newr, newc, d + 1))
                            grid[newr][newc] = min(d + 1, val)


