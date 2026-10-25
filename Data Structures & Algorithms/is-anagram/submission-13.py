class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = defaultdict(int)
        for x, y in zip(s,t):
            hashmap[x] += 1
            hashmap[y] -= 1
        
        for _, v in hashmap.items():
            if v != 0:
                return False
        
        return True