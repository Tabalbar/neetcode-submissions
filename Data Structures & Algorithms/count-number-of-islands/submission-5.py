class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()

        num_islands = 0

        def bfs(i,j):
            q = deque()
            q.append((i,j))
            visited.add((i,j))

            while len(q) > 0:
                print(q, visited)
                curr = q.popleft()
                for dr, dc in dirs:
                    n = (curr[0] + dr, curr[1] + dc)
                    if n[0] >= 0 and n[1] >= 0 and n[0] < rows and n[1] < cols and (n[0],n[1]) not in visited and grid[n[0]][n[1]] == "1":
                        q.append((n[0],n[1]))
                    visited.add((n[0],n[1]))
                         

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    num_islands += 1

        return num_islands