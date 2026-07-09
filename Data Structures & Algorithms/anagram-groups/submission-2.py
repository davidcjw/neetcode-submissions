class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution 1: sorting
        # Time: n * k log k
        # Space: n * k
        res = defaultdict(list)
        for s in strs:
            res["".join(sorted(s))].append(s)
        return list(res.values())
