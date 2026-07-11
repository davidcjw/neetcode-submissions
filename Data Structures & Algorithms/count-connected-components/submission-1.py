class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        rank = [1] * n
        res = n # worst case, number of components = number of vertices

        def find(node):
            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]
            return node
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                rank[p2] += rank[p1]
                parents[p1] = p2
            else:
                rank[p1] += rank[p2]
                parents[p2] = p1
            return 1

        for i, j in edges:
            res -= union(i,j)
        
        return res