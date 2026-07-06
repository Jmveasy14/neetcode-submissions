from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0
        def bfs(row,col):
            queue = deque([(row,col)])
            visited.add((row,col))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            while queue:
                (r,c) = queue.popleft()
                for dr,dc in directions:
                    neighbor_r = r + dr
                    neighbor_c = c + dc
                    if ((0<= neighbor_r < ROWS) and (0 <= neighbor_c < COLS) and ((neighbor_r,neighbor_c) not in visited) and grid[neighbor_r][neighbor_c] == '1'):
                        queue.append((neighbor_r,neighbor_c))
                        visited.add((neighbor_r,neighbor_c))
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        
        return islands