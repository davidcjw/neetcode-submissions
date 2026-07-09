class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution 1: sorting
        # Time: n * k log k
        # Space: n * k
        # res = defaultdict(list)
        # for s in strs:
        #     res["".join(sorted(s))].append(s)
        # return list(res.values())

        # Solution 2: Using fixed size list
        # Time: n * k
        # Space: n
        res = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for char in s:
                key[ord(char) - ord('a')] += 1
            res[tuple(key)].append(s)

        return list(res.values())
