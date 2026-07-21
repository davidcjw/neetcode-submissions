class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # core idea: i don't care what to replace, i only know how
        # many i can replace
        l = 0
        counter = defaultdict(int)
        max_len = 0

        # window size = r-l+1
        for r in range(len(s)):
            counter[s[r]] += 1

            # if window has more changes than needed, move left pointer
            while (r-l+1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r-l+1)
        
        return max_len