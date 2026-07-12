class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # what does valid mean? 
        # 1) no cycles and 2) fully connected
        parents = list(range(n))
        rank = [1] * n

        def find(node):
            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]
            return node

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                rank[p1] += 1
                parents[p2] = parents[p1]
            else:
                rank[p2] += 1
                parents[p1] = parents[p2]
            return True

        n_components = n
        for n1, n2 in edges:
            if not union(n1, n2):
                return False
            n_components -= 1

        return n_components == 1