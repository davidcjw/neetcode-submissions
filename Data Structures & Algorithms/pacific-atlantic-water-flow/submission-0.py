class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIRECTIONS = [(0,1),(1,0),(-1,0),(0,-1)]
        r, c = len(heights), len(heights[0])
        # start from pacific and atlantic
        pacific_start=[(0,i) for i in range(c)] + [(i,0) for i in range(r)]
        atlantic_start=[(r-1,i) for i in range(c)] + [(i,c-1) for i in range(r)]

        pac = set()
        atl = set()
        def dfs(x,y,visit,prevHeight):
            if x < 0 or x == r or y < 0 or y == c or (x,y) in visit or heights[x][y] < prevHeight:
                return
            visit.add((x,y,))
            for dx, dy in DIRECTIONS:
                xx, yy = dx+x, dy+y
                dfs(xx,yy,visit,heights[x][y])

        print(pacific_start,atlantic_start)
        for coord in pacific_start:
            x, y = coord
            dfs(x,y,pac,heights[x][y])
        for coord in atlantic_start:
            x, y = coord
            dfs(x,y,atl,heights[x][y])

        res = []
        for i in range(r):
            for j in range(c):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])

        return res
            