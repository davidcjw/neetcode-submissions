class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # naive solution: iterate through each word and sort each word
        # then create a hashmap based on the sorted word
        # time: O(m*n log n)
        # space: O(m*n)
        # seen = defaultdict(list)
        # for s in strs:
        #     seen["".join(sorted(s))].append(s)

        # return list(seen.values())

        # method 2: use occurences of chars as keys
        # [{}, {}, ..., {}]
        res = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord(char) - ord('a')] += 1
            res[tuple(counts)].append(s)
        return list(res.values())