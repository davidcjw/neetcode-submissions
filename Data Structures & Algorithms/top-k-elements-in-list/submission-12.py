class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a hashmap {1: 10, 1000: 3}
        # time: O(n + n log n) = O(n log n)
        # space: O(n)
        # res = defaultdict(int)
        # for num in nums:
        #     res[num] += 1
        
        # return list(dict(sorted(res.items(), key=lambda x: x[1], reverse=True)).keys())[:k]

        # min heap
        # create hash map of counts: O(n)
        # building heap = O(n)
        # time: O(n)
        # space: O(n)
        res = defaultdict(int)
        for num in nums:
            res[num] += 1

        min_heap = []
        for key, val in res.items():
            heapq.heappush(min_heap, (val, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
    
        print(min_heap, key)
        return [val for key, val in min_heap]
