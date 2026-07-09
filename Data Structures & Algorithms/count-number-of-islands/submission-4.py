from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            queue = deque([(r,c)])
            visited.add((r,c))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            while queue:
                curr_r,curr_c = queue.popleft()
                for dr,dc in directions:
                    neighbor_r = curr_r + dr
                    neighbor_c = curr_c + dc
                    if (0 <= neighbor_r <ROWS) and (0 <= neighbor_c < COLS) and grid[neighbor_r][neighbor_c] == '1' and( (neighbor_r,neighbor_c) not in visited):
                        queue.append((neighbor_r,neighbor_c))
                        visited.add((neighbor_r,neighbor_c))
            return
                


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands
        