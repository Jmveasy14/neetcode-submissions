from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        result = 0
        visited = set()

        def bfs(r,c):
            queue = deque([(r,c)])
            visited.add((r,c))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            
            while queue:
                curr_r,curr_c = queue.popleft()
                for dr,dc in directions:
                    neighbor_r = dr + curr_r
                    neighbor_c = dc + curr_c
                    if 0 <= neighbor_r < ROWS and 0 <= neighbor_c < COLS and (neighbor_r,neighbor_c) not in visited and grid[neighbor_r][neighbor_c] == '1':
                        queue.append((neighbor_r,neighbor_c))
                        visited.add((neighbor_r,neighbor_c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)

                    result +=1
                    
        return result