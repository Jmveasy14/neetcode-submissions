"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if intervals:
            intervals.sort(key =lambda i: i.start )
            curr = intervals[0]
        for i in range(1,len(intervals)):
            if curr.end <= intervals[i].start:
                curr = intervals[i]
            else:
                return False
        return True
