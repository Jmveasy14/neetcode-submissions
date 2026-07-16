from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        max_area = 0

        def bfs(row,col):
            queue = deque([(row,col)])
            visited.add((row,col))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            area = 1

            while queue:
                (curr_r,curr_c) = queue.popleft()
                for (r,c) in directions:
                    neighbor_r = curr_r + r
                    neighbor_c = curr_c + c
                    if (0<= neighbor_r < ROWS) and (0<= neighbor_c < COLS) and ((neighbor_r,neighbor_c) not in visited )and (grid[neighbor_r][neighbor_c] == 1):
                        area+=1
                        queue.append((neighbor_r,neighbor_c))
                        visited.add((neighbor_r,neighbor_c))
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area,(bfs(r,c)))
        return max_area