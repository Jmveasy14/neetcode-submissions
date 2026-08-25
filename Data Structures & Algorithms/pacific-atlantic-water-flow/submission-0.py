class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        atl = set()
        r = 0
        c = 0
        result = []

        def dfs(r,c, prev, visited):
            if not (0<= r < ROWS and 0<= c< COLS):
                return   
            if  (heights[r][c] < prev or (r,c) in visited):
                return
            visited.add((r,c))
            prev = heights[r][c]
        
            dfs(r,c+1,heights[r][c],visited)
            dfs(r,c-1,heights[r][c],visited)
            dfs(r+1,c,heights[r][c],visited)
            dfs(r-1,c,heights[r][c],visited)


        for r in range(ROWS):
            dfs(r,0,heights[r][0],pac)
            dfs(r,COLS -1,heights[r][COLS-1],atl)

        for c in range(COLS):
            dfs(0,c,heights[0][c],pac)
            dfs(ROWS-1,c,heights[ROWS-1][c],atl)
            

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])
        
        return result


        
