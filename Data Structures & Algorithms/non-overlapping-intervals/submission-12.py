class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals.sort(key = lambda i: i[1])

        prev_end = intervals[0][1]
        result = 0

        for start,end in intervals[1:]:
            if start < prev_end:
                result+=1
            else:
                prev_end = end
        
        return result

        