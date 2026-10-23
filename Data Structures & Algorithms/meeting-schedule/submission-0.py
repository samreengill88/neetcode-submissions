"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        # sort interval by start times
        intervals.sort(key=lambda x:x.start)

        for i in range(1, len(intervals)):
            prev_interval = intervals[i - 1]
            curr_interval = intervals[i]

            if prev_interval.end > curr_interval.start:
                return False
        return True