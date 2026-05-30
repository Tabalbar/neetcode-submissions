class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = []
        q = deque()
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        #[(1,1), .. ,...]
        # curr = (0,1)
        # visited = (0,1), (1,1)
        # neighbors of curr (1,1), (0,2), (-1,1) (0,0)

        def bfs(i, j):
            q.append((i,j))
            area = 1
            while len(q) > 0:
                curr = q.popleft()
                visited.append((curr[0], curr[1]))
                for r, c in dirs:
                    neighbor = (curr[0] + r, curr[1] + c)
                    dr, dc = neighbor[0], neighbor[1]
                    if dr >= 0 and dc >= 0 and dr < rows and dc < cols and (dr,dc) not in visited:
                        visited.append((dr, dc))
                        if grid[dr][dc] == 1:
                            q.append((dr, dc))
                            area +=1
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = bfs(i,j)
                    if area > max_area:
                        max_area = area

        return max_area