class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        l, r = 0, window_len

        s1 = "".join(sorted(s1))
        while r <= len(s2):
            windowStr = s2[l:r]
            if s1 == "".join(sorted(windowStr)):
                return True
            
            l += 1
            r += 1
        
        return False
