from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()

        def bfs(start_row,start_col):
            area = 1
            queue = deque([(start_row,start_col)])
            visited.add((start_row,start_col))
            
            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            while queue:
                curr_r,curr_c = queue.popleft()
                for row,col in directions: 
                    neighbor_r = curr_r + row
                    neighbor_c = curr_c + col

                    if (0 <=neighbor_r < len(grid) and 0<= neighbor_c < len(grid[0])) and (grid[neighbor_r][neighbor_c] == 1) and ((neighbor_r,neighbor_c) not in visited):
                        queue.append((neighbor_r,neighbor_c))
                        visited.add((neighbor_r,neighbor_c))
                        area+=1
            return area


        max_area = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r,c) not in visited:
                    curr_area = bfs(r,c)
                    max_area = max(max_area,curr_area)
        
        return max_area