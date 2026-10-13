class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited = set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                #if we find an empty space
                if val == '.':
                    continue

                row_key = ('row',r,val)
                col_key = ('col',c,val)
                box_key = (r//3,c//3,val)

                if row_key in visited or col_key in visited or box_key in visited:
                    return False
                visited.add(row_key)
                visited.add(col_key)
                visited.add(box_key)
        return True