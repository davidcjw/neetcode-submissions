class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        DIRECTIONS = [(-1,0),(1,0),(0,1),(0,-1)]
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if (i,j) in visited or grid[i][j] == 0:
                    continue
                
                stack = [(i,j)]
                visited.add((i,j))
                area = 0
                while stack:
                    x, y = stack.pop()
                    area += 1
                    for dx, dy in DIRECTIONS:
                        xx, yy = dx+x, dy+y
                        if 0 <= xx < m and 0 <= yy < n and (xx,yy) not in visited and grid[xx][yy] == 1:
                            stack.append((xx,yy))
                            visited.add((xx,yy))
                
                maxArea = max(maxArea, area)

        return maxArea