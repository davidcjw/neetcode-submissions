class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 4; prereqs: [[2,3],[3,4],[3,2],[1,3],[0,4]]
        # {2: [3], 1: [3], 0: [4], 3: [2,4]}
        # if a course is not in adjacency list, means it can be completed on its own
        # 1) detect any cycle, then return empty array
        # 2) add in courses that have no deps to anywhere in the result array
        # 0 -> 1 -> 2 -> 3 -> 0
        # 0 -> 1; 0 -> 2 -> 3 -> 2
        res = []
        adj_list = defaultdict(list)
        UNVISITED, VISITING, VISITED = 0, 1, 2
        visited = [UNVISITED] * numCourses

        # build adjacency list
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        # start from any course say 0
        def dfs(course):
            if visited[course] == VISITING:
                return False
            if visited[course] == VISITED:
                return True
            visited[course] = VISITING
            courseDeps = adj_list[course]
            for dep in courseDeps:
                if not dfs(dep):
                    return False
            res.append(course)
            visited[course] = VISITED
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res
        # return res[::-1]