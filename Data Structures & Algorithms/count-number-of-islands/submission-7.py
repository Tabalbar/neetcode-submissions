class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0
        visited = {}
        neighbors = [(1,0), (0,1), (-1,0), (0,-1)]

        def bfs(i,j):
            q = deque()
            visited[(i,j)] = 1
            q.append((i,j))

            while len(q) > 0:
                poi = q.popleft() # poi = part of island
                print(f'poi {poi}')
                for dr, dc in neighbors:
                    poi_i, poi_j = poi[0] + dr, poi[1] + dc
                    print(f'neighbor {(poi_i, poi_j)}')
                    if (poi_i >= 0 and poi_j >= 0 and poi_i < rows and poi_j < cols and 
                        (poi_i, poi_j) not in visited and grid[poi_i][poi_j] == "1"):
                        visited[(poi_i, poi_j)] = 1
                        q.append((poi_i, poi_j))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    print(f'called with {(i,j)}')
                    bfs(i,j)
                    num_islands += 1

        return num_islands
        