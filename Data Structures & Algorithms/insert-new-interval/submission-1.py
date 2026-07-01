class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []

        for i in range(len(intervals)):
            #if the end point of the new interval is smaller than the current interval tehn it goes before
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result+intervals[i:]
            
            #if the start point of the new interval is greater than the end of the current interval then it goes after
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            #If neither is the case then we found an overlapping interval
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(intervals[i][1],newInterval[1])]

        result.append(newInterval)
        return result
