class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # pencilcase ["pencil", "pen", "case"]
        memo = {}

        def dfs(word):
            if not word:
                return True

            if word in memo:
                return memo[word]

            for w in wordDict:
                w_len = len(w)
                if word[:w_len] == w:
                    if dfs(word[w_len:]):
                        memo[word] = True
                        return True

            memo[word] = False
            return False

        return dfs(s)
