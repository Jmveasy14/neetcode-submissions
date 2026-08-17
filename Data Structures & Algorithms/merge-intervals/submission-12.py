class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])

        if len(intervals) == 1:
            return intervals
        result = []
        prev = intervals[0]

        for inter in intervals[1::]:
            if prev[1] < inter[0]:
                result.append(prev)
                prev = inter
            else:
                prev = [prev[0],max(prev[1],inter[1])]
        result.append(prev)
        return result
            
        