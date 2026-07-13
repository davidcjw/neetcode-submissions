class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # [(1,30),(2,3),(3,4),(4,5)]
        # [(1,10),(2,6),(3,7),(4,8)]
        # greedy approach - remove intervals that end later
        max_end = intervals[0][1]
        counts = 0
        for start, end in intervals[1:]:
            if start >= max_end:
                max_end = end
            else:
                counts += 1
                max_end = min(end, max_end)

        return counts
