class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time_taken = 0

        adj_list = defaultdict(list)
        for time in times:
            start, end, t = time
            adj_list[start].append((end, t))

        # BFS - use queue
        visited = set()
        minHeap = [(0, k)]
        while minHeap:
            weight, start = heapq.heappop(minHeap)
            if start in visited:
                continue
            
            visited.add(start)
            time_taken = max(time_taken, weight)

            for neighbour, neighbour_weight in adj_list[start]:
                if neighbour not in visited:
                    heapq.heappush(minHeap, (neighbour_weight+weight, neighbour))

        return time_taken if len(visited) == n else -1