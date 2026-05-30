class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def get_area_bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r, c))
            area = 1
            while len(q) > 0:
                curr_r, curr_c = q.popleft()
                print((curr_r, curr_c))
                directions = [(1,0), (0,1), (-1,0), (0,-1)]
                for dir_r, dir_c in directions:
                    new_r, new_c = dir_r + curr_r, dir_c + curr_c
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 1 and (new_r, new_c) not in visited:

                        area += 1
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))
            return area

        for row in range(rows):
            for col in range(cols):
                print(row, col)
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = get_area_bfs(row,col)
                    if area > max_area:
                        max_area = area
        return max_area