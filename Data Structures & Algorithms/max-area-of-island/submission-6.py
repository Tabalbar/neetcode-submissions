class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        maxArea = 0

        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        visited = set()
        queue = deque([])

        def bfs(r,c):
            nonlocal maxArea
            queue.append((r,c))
            visited.add((r,c))
            area = 1
            while len(queue) > 0:
                i,j = queue.popleft()
                for dirr, dirc in dirs:
                    newr, newj = i + dirr, j + dirc
                    if newr >= 0 and newj >= 0 and newr < rows and newj < cols:
                        val = grid[newr][newj]
                        if val == 1 and (newr,newj) not in visited:
                            area += 1
                            queue.append((newr,newj))
                            visited.add((newr,newj))

                maxArea = max(maxArea, area)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs(r,c)

        return maxArea