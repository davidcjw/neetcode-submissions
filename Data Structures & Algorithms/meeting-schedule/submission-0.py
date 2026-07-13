class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # O(n log n) solution: sort first then iterate and compare
        if len(intervals) <= 1:
            return True
        
        flattened = []
        for interval in intervals:
            flattened.append((interval.start, interval.end))
        flattened.sort()
        curr = flattened[0]
        for i in range(1, len(flattened)):
            curr_start, curr_end = curr
            if flattened[i][0] >= curr_start and flattened[i][0] < curr_end:
                return False
            curr = flattened[i]
        
        return True
