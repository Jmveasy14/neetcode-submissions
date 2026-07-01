class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #inserting new interval
        #intervals = [[1,3],[4,6]], newInterval = [2,5]
        result = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
                   
        #if the new intervals end point is greater than the current start point
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            else:
                newInterval = [min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
        result.append(newInterval)
        return result


        

        


        
        
        