class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # naive solution: iterate through each word and sort each word
        # then create a hashmap based on the sorted word
        # time: O(m*n log n)
        # space: O(m*n)
        seen = defaultdict(list)
        for s in strs:
            seen["".join(sorted(s))].append(s)

        return list(seen.values())