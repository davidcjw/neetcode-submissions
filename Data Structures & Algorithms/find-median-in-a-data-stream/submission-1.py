class MedianFinder:

    def __init__(self):
        self.min_heap = []  # stores larger half
        self.max_heap = []  # stores smaller half
        self.size = len(self.min_heap) + len(self.max_heap)

    def addNum(self, num: int) -> None:
        # [1,2,3,4,5]
        # min_heap = [4,5], max_heap = [1,2,3]
        # [3,5] [1]
        # we need to make sure that min_heap has strictly larger
        # values than max_heap

        # empty case
        if not self.max_heap and not self.min_heap:
            heapq.heappush(self.min_heap, num)
        elif num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
            self.rebalanceHeaps()
        else:
            heapq.heappush(self.max_heap, -num)
            self.rebalanceHeaps()
        self.size += 1

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            # use minus sign since max_heap is negative
            return (self.min_heap[0] - self.max_heap[0]) / 2
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]

    def rebalanceHeaps(self) -> None:
        # length should not differ by more than 1
        diff = len(self.max_heap) - len(self.min_heap)
        if abs(diff) <= 1:
            return
        
        # rebalance
        numElementsToPop = abs(diff) - 1
        if diff > 0:  # rebalance from max_heap to min_heap
            for i in range(numElementsToPop):
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        else:
            for i in range(numElementsToPop):
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
