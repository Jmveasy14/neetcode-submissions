class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda i: i[0])
        result = []
        #[1,2],[3,5],[5,8]

        #if we find intervals that overlap, add the window to the result 

        #if they dont overlap then
        prev = intervals[0]
#[1,3], [4,5]


        for i in range(1,len(intervals)):
            curr = intervals[i]
            if prev[1] >= curr[0]:
                prev = [prev[0], max(prev[1],curr[1])]
            else:
                result.append(prev)
                prev = curr
        result.append(prev)
        return result
          


            


        #
        