class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = defaultdict(int)
        for char in s:
            s_counts[char] += 1
        
        for char in t:
            s_counts[char] -= 1
        
        for _, v in s_counts.items():
            if v != 0:
                return False
        
        return True