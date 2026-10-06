class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #when we find a 1, its an island
        #dfs it and count the number of 1s in that island
        #compare it to the max
        #need to keep track of size of current island (idk if i do that in the dfs or outside, im assuming outside)
        # return the max
        row = len(grid)
        col = len(grid[0])
        visited = set()
        max_area = 0
        def dfs(curr_r,curr_c):
            if 0 <= curr_r < len(grid) and 0<= curr_c < len(grid[0]) and grid[curr_r][curr_c] == 1 and (curr_r,curr_c) not in visited:

                visited.add((curr_r,curr_c))

                return 1 + dfs(curr_r+1,curr_c) + dfs(curr_r-1,curr_c) + dfs(curr_r,curr_c+1) + dfs(curr_r,curr_c-1) 
            
            return 0
            
            


        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area,dfs(r,c))

        return max_area
