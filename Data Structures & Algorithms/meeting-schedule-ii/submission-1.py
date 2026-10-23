"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # sort intervals by start times
        intervals.sort(key=lambda x:x.start)

        # rooms is min_heap with end times -> event finishing latest at top
        rooms = []

        for interval in intervals:
            
            # if room event has already finished before the curr interval start time
            # pop the room - no longer needed 

            if rooms and rooms[0] <= interval.start:
                heapq.heappop(rooms)

            # push end time to heap
            heapq.heappush(rooms, interval.end)
        return len(rooms)
    
    # TC: O(n log n)
    # SC: O(n)