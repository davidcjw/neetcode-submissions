class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams -> track word counts
        # limited space O(26) at most
        track = defaultdict(int)
        for a in s:
            track[a] += 1
        
        for b in t:
            track[b] -= 1

        for k,v in track.items():
            if v != 0:
                return False
        
        return True