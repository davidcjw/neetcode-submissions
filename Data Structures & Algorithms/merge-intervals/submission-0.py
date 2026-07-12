class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # input is not necessarily sorted
        # [[3,5], [1,3], [2,7], [8,9]]
        # [[1,7], [8,9]]
        # solution 1: sort based on starting time O(n log n)
        # [[1,3],[2,7],[3,5],[8,9]]
        # as long as starting time is between start & end time,
        # the intervals will merge then take larger end time of the two
        intervals.sort()
        res = []
        curr = intervals[0]
        for start, end in intervals:
            if start >= curr[0] and start <= curr[1]:
                curr[1] = max(curr[1], end)
            else:
                res.append(curr)
                curr = [start,end]
            
        if curr:
            res.append(curr)

        return res
