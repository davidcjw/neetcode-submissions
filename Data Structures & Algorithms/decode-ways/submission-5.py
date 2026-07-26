class Solution:
    def numDecodings(self, s: str) -> int:
        """
        A -> 1
        B -> 2
        ...
        J -> 10
        K -> 11
        ...
        T -> 20
        U -> 21
        ...
        Z -> 26

        10429 -> 1,04 X; 10,4,2,9; 10,42 X; 10,4,29 X, 10,4,2,9
        if num starts with 1 or 2, need to DFS both paths 1/1X and 2/2X
        For 2, only up to 26
        n = 5
        """
        memo = {}

        def dfs(i):
            n = len(s)
            if i >= n:
                return 1
            if i in memo:
                return memo[i]
            
            if s[i] == "0":
                memo[i] = 0
                return 0
            
            ways = dfs(i+1)
            if i+1 < n and s[i] == "1":
                ways += dfs(i+2)
            elif i+1 < n and s[i] == "2" and s[i+1] <= "6":
                ways += dfs(i+2)

            memo[i] = ways
            return ways

        return dfs(0)