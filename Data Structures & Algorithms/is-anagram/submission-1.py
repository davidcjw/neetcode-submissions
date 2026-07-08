class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dictionary to track counts of each character
        # max we have 26 different characters
        # time: O(s+t)
        # space: O(26)
        seen_s = defaultdict(int)
        seen_t = defaultdict(int)
        for char in s:
            seen_s[char] += 1
        for char in t:
            seen_t[char] += 1
        if seen_s == seen_t:
            return True
        return False