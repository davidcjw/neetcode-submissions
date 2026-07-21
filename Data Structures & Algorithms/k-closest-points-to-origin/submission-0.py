class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        def euclidean_distance(x, y):
            return math.sqrt((x-0)**2 + (y-0)**2)

        min_heap = []
        for point in points:
            x, y = point
            heapq.heappush(min_heap, (euclidean_distance(x,y), point))
        
        for i in range(k):
            _, point = heapq.heappop(min_heap)
            res.append(point)

        return res
