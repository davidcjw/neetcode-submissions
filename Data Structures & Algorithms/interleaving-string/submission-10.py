class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def dfs(s1, s2, s3):
            m, n, o = len(s1), len(s2), len(s3)
            if m + n != o:
                return False
            if m == 0 and n == 0 and o == 0:
                return True

            if (s1,s2,s3) in memo:
                return memo[(s1,s2,s3)]

            path1 = s1 and s1[0] == s3[0] and dfs(s1[1:], s2, s3[1:])
            path2 = s2 and s2[0] == s3[0] and dfs(s1, s2[1:], s3[1:])
            memo[(s1,s2,s3)] = path1 or path2

            return memo[(s1,s2,s3)]

        res = dfs(s1, s2, s3)
        return res if res else False
