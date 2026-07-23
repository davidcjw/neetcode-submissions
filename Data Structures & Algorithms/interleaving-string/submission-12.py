class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, o = len(s1), len(s2), len(s3)
        if m + n != o:
            return False

        memo = {}
        def dfs(i, j):
            if i == m and j == n:
                return True
            if (i,j) in memo:
                return memo[(i,j)]

            k = i + j
            path1 = i < m and s1[i] == s3[k] and dfs(i+1, j)
            path2 = j < n and s2[j] == s3[k] and dfs(i, j+1)
            memo[(i,j)] = path1 or path2

            return memo[(i,j)]

        return dfs(0, 0)
        # res = dfs(s1, s2, s3)
        # return res if res else False
