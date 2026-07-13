class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # only if overlapping then need 2 meeting rooms
        # is it essentially asking how many times meetings overlap? not really.
        # [(0, 1),(4,10),(2,4),(3,5)]
        # [(0,1),(2,4),(3,5),(4,10)]
        # [(1,5),(2,4)]
        # use stack to hold end times; if next start time >= next end time on stack, pop and remove 1
        # nono, use min heap
        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key=lambda i: i.start)
        end_times = [intervals[0].end]

        for i in range(1, len(intervals)):
            if end_times and intervals[i].start >= end_times[0]:
                heapq.heappop(end_times)
            heapq.heappush(end_times, intervals[i].end)
        
        return len(end_times)
