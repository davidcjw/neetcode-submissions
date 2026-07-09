class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a hashmap {1: 10, 1000: 3}
        # time: O(n^2 log n)
        # space: O(n)
        res = defaultdict(int)
        for num in nums:
            res[num] += 1
        
        return list(dict(sorted(res.items(), key=lambda x: x[1], reverse=True)).keys())[:k]
