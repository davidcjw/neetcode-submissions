class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maintain a min heap of size k
        # [1,2,3,4,5]
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]