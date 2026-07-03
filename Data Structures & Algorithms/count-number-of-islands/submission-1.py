from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        visited = set()

        #we go through the grid and once we find a 1, we need to see how large the island is
        def bfs(row,col):
            queue = deque([(row,col)])
            visited.add((row,col))
            
            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            #check bounds and add to visited
            while queue:
                curr_r, curr_c = queue.popleft()
                for r, c in directions:
                    neighbor_r = curr_r +r
                    neighbor_c = curr_c +c
                    if ((0 <= neighbor_r <len(grid)) and (0 <= neighbor_c < len(grid[0]))and (grid[neighbor_r][neighbor_c] == '1') and ((neighbor_r,neighbor_c) not in visited)):
                        visited.add((neighbor_r,neighbor_c))
                        queue.append((neighbor_r,neighbor_c))
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1

        return islands
        