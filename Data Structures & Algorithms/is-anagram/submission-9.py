class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = [0] * 26
        for x, y in zip(s,t):
            counts[ord(x) - ord('a')] += 1
            counts[ord(y) - ord('a')] -= 1
        
        return all(c == 0 for c in counts)