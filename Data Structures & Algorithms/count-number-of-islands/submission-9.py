class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        visited = set()

        ROWS = len(grid)
        COLS = len(grid[0])

        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        num_islands = 0

        def dfs(i, j):
            q.append((i,j))
            while len(q) > 0:
                node = q.popleft()
                visited.add((node[0], node[1]))
                for dr, dc in dirs:
                    new_node = (node[0] + dr, node[1] + dc)
                    if (new_node[0] >= 0 and new_node[0] < ROWS and 
                    new_node[1] >= 0 and new_node[1] < COLS and 
                    (new_node[0], new_node[1]) not in visited and
                    grid[new_node[0]][new_node[1]] == "1"):
                        q.append(new_node)


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    num_islands += 1

        return num_islands