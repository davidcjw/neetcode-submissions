class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s="abcabcbb"
        # s=”baca”
        if not s:
            return 0

        l, r = 0, 0
        res = 0
        seen = set()
        while r < len(s):
            char = s[r]
            if char not in seen:
                seen.add(char)
            else:
                res = max(res, r-l)
                while s[l] != char:
                    seen.remove(s[l])
                    l += 1
                l += 1 # skip past the dupe itself
            r += 1
        return max(res, r-l)
