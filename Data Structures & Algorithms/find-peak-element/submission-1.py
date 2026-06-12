class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #Iterate through the list
        #compare values with indexes on the right and left of val
        #if it is greater than left and smaller than right its valid
        #keep looking

        
        
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = (left+right) //2

            #left neighbor is greater
            if mid > 0 and nums[mid] < nums[mid -1]:
                right = mid-1
                #right neighbor is greater
            elif mid < len(nums) - 1 and nums[mid] < nums[mid +1]:
                left = mid+1
            else:
                return mid

        