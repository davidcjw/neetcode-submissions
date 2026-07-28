class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # At every cell:
        #   1) Check current 3x3
        #   2) Check current row
        #   3) Check current column
        # If a row is checked, don't have to check it again. Likewise for col
        # Alternatively, we could do row checks first, then col. 
        # Then 3x3s
        # rows: {0: set(1,2,3), 1: set(4,5), 2: set(8,9,3), ...}
        # cols: {0: set(1,4,5,7), 1: set(2,9)}
        # threeByThree: {2: set(3)}
        rows = defaultdict(set)
        cols = defaultdict(set)
        threeByThree = defaultdict(set)
        N_ROWS = N_COLS = 9

        for i in range(N_ROWS):
            for j in range(N_COLS):
                val = board[i][j]
                if val == ".": continue
                if val in rows[i] or val in cols[j] or val in threeByThree[self.getQuadrant(i,j)]:
                    print((i,j),rows,cols,threeByThree)
                    return False
                rows[i].add(val)
                cols[j].add(val)
                threeByThree[self.getQuadrant(i,j)].add(val)

        return True
    
    def getQuadrant(self, i, j) -> int:
        # quadrants are also 0-indexed
        if i <= 2:
            if j <= 2:
                return 0
            elif 2 < j <= 5:
                return 1
            else:
                return 2
        elif 2 < i <= 5:
            if j <= 2:
                return 3
            elif 2 < j <= 5:
                return 4
            else:
                return 5
        else:
            if j <= 2:
                return 6
            elif 2 < j <= 5:
                return 7
            else:
                return 8
        
                