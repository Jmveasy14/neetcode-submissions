class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #If letters connect vertically or horizontally to create a word
        #Return true
        ROW = len(board)
        COL = len(board[0])

        def dfs(row,col,index):
            
            
            if index == len(word):
                return True

            elif row < 0 or row >= ROW or col < 0 or col >= COL or board[row][col] != word[index]:
                return False 
            
            temp = board[row][col]

            board[row][col] = '#'
            
            

            for dr,dc in[(-1,0),(1,0),(0,-1),(0,1)]:
                
                if dfs(row+dr,col+dc,index+1):
                    board[row][col] = temp
                    return True
            else:
                board[row][col] = temp
                return False
            


        for r in range(ROW):
            for c in range(COL):
                #If we find the first character we need to look for next charcter to see if its adjacent
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False


                #dfs on grid for each correspong letter

        