class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # O(n log n) solution: sort first then iterate and compare
        if len(intervals) <= 1:
            return True
        
        intervals.sort(key=lambda i: i.start)
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i].start >= curr.start and intervals[i].start < curr.end:
                return False
            curr = intervals[i]
        
        return True
