class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = []
        num_islands = 0

        def bfs(i,j):
            dirs = [(1,0), (0,1), (-1,0), (0,-1)]
            q = deque()
            q.append((i,j))
            visited.append((i,j))

            while len(q) > 0:
                node = q.popleft()
                for d in dirs:
                    new_node = (node[0] + d[0], node[1] + d[1])
                    if new_node[0] >= 0 and new_node[0] < rows and new_node[1] >= 0 and new_node[1] < cols and new_node not in visited:
                        visited.append(new_node)
                        if grid[new_node[0]][new_node[1]] == "1":
                            q.append(new_node)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    num_islands +=1
        print(num_islands)
        return num_islands