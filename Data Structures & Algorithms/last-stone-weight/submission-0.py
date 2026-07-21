class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        # at each step, take two heaviest stones out
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if y-x > 0:
                heapq.heappush(maxHeap, x-y)

        if len(maxHeap) == 1:
            return -maxHeap[0]
        return 0
