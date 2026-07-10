class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        for idx, _ in enumerate(s):
            seen = set()
            for i in range(idx, len(s)):
                if s[i] not in seen:
                    seen.add(s[i])
                else:
                    break
        
                max_len = max(max_len, len(seen))
        print(seen)
        max_len = max(max_len, len(seen))
        return max_len
