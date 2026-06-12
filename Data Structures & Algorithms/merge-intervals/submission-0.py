class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        
        result = [intervals[0]]

        for i in range(len(intervals)):
            if intervals[i] == result[0]:
                continue
            
            elif result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1],intervals[i][1])
            else:
                result.append(intervals[i])
        
        return result
        