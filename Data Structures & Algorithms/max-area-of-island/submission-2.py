class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        max_area = 0
        

        def dfs(r,c):
            count = 0
            if not(0<= r < ROWS and 0<=c < COLS and grid[r][c] == 1 and (r,c) not in visited):
                return 0
            visited.add((r,c))
            return 1 + (
            dfs(r,c+1)
            + dfs(r,c-1)
            + dfs(r+1,c)
            + dfs(r-1,c) )

            return count
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:

    
                    max_area = max(max_area,dfs(r,c))
        
        return max_area


        