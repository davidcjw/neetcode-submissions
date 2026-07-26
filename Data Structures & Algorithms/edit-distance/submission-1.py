class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[None] * n for _ in range(m)]

        def dfs(i, j):
            # if reach end of word1, the edit distance is the diff between the remaining chars of word2
            if i == m:
                return n - j
            # if reach end of word2, the edit distance is the diff between the remaining chars of word1
            if j == n:
                return m - i
            if dp[i][j] is not None:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = dfs(i+1, j+1)
            else:
                insert = dfs(i, j+1) + 1
                delete = dfs(i+1, j) + 1
                replace = dfs(i+1, j+1) + 1
                dp[i][j] = min([insert, delete, replace])

            return dp[i][j]

        return dfs(0,0)
        