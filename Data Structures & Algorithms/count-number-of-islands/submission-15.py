class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        queue = deque([])
        count = 0

        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def bfs(r,c):
            visited[(r,c)] = 1
            queue.append((r,c))

            while len(queue) > 0:
                i, j = queue.popleft()
                for dr, dc in dirs:
                    newr = i + dr
                    newc = j + dc
                    
                    if newr >= 0 and newr < rows and newc >= 0 and newc < cols:
                        val = grid[newr][newc]
                        if val == "1" and (newr,newc) not in visited:
                            queue.append((newr,newc))
                            visited[(newr,newc)]=1



        for r in range(rows):
            for c in range(cols):
                val = grid[r][c]
                if val == "1" and (r,c) not in visited:
                    count += 1
                    bfs(r,c)

        return count

        