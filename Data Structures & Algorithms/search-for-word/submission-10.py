class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, charIdx):
            DIRECTIONS = [(-1,0),(1,0),(0,1),(0,-1)]
            if board[x][y] != word[charIdx]:
                return False
            if charIdx == len(word)-1:
                return True

            temp = board[x][y]
            board[x][y] = "#"  # mark as used

            for dx, dy in DIRECTIONS:
                xx, yy = dx+x, dy+y
                if 0 <= xx < r and 0 <= yy < c and dfs(xx, yy, charIdx+1):
                    board[x][y] = temp  # restore to original
                    return True
            
            board[x][y] = temp  # backtrack: cell is usable again
            return False
        
        r, c = len(board), len(board[0])

        for i in range(r):
            for j in range(c):
                if dfs(i, j, 0):
                    return True
        return False
