class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for course, dep in prerequisites:
            adj_list[course].append(dep)


        UNVISITED, VISITING, VISITED = 0, 1, 2
        state = [UNVISITED] * numCourses

        def dfs(node):
            if state[node] == VISITING:
                return False # cycle detected
            if state[node] == VISITED:
                return True
            state[node] = VISITING
            for neighbour in adj_list[node]:
                if not dfs(neighbour):
                    return False
            state[node] = VISITED
            return True
            
        return all(dfs(i) for i in range(numCourses))
