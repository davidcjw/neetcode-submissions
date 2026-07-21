class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = defaultdict(list)
        total_price = 0

        for source, destination, price in flights:
            edges[source].append((destination, price))

        minHeap = [(0, 0, src)]
        visited = set()
        while minHeap:
            print(minHeap, visited)
            price, stop, sourceEdge = heapq.heappop(minHeap)
            
            # don't allow updating price and visited if stops exceed allowed
            if stop > k+1:
                continue

            total_price = max(total_price, price)
            visited.add(sourceEdge)

            if dst in visited:
                break

            for neighbour, px in edges[sourceEdge]:
                if neighbour not in visited:
                    print('adding', neighbour)
                    heapq.heappush(minHeap, (px+price, stop+1, neighbour))

        if dst in visited:
            return total_price
        return -1