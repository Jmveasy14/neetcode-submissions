"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        s = 0
        e = 0
        active_meetings = 0
        max_rooms = 0
        res = 0
       
        for time in intervals:
            starts.append(time.start)
            ends.append(time.end)
            
        starts.sort()
        ends.sort()

        while s < len(intervals):
            if starts[s] < ends[e]:

                
                s+=1
                active_meetings+=1
            else:
                active_meetings-=1
                e+=1
            
            max_rooms = max(max_rooms,active_meetings)
        
        return max_rooms




        