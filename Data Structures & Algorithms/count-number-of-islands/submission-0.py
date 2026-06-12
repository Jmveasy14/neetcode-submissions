from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])    
        islands = 0
        visited = set()
        

        def bfs(r,c):
            queue = deque()

            visited.add((r,c))
            queue.append((r,c))

            while queue:
                row,col = queue.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    r,c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c] == "1" and (r, c) not in visited):
                        queue.append((r,c))
                        visited.add((r,c))
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1 

         
        return islands 

                    

        #we check for 1s and if we find one, see how long it goes until we find another zero
        #then once we find a zero we know thats the width of first row
        #We check if there are 1s directly under the first row 1s and go on till we find a zero
        #if the 1s are connected and surrounded by zeroes, we add the island_counter by 1
        # we the check the rest

        # 
                


        