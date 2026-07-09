class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        num_islands = 0
        directions = [(1,0), (0,1), (-1,0),(0,-1)]
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in visited:
                    num_islands += 1
                    visited.add((i,j))

                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in directions:
                            xx, yy = x+dx, y+dy
                            if 0 <= xx < n and 0 <= yy < m and grid[xx][yy] == "1" and (xx, yy) not in visited:
                                stack.append((xx,yy))
                                visited.add((xx,yy))

        return num_islands
