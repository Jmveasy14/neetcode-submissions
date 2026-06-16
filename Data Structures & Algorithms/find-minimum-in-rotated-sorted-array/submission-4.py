class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        minimum = nums[0]

        left = 0
        right = len(nums) -1
        #[3,4,5,6,7,1,2]
        #[1,2,3,4,5,6,7]


        while left <= right:
            mid = (left+right) //2

            if nums[mid] < minimum:
                minimum = nums[mid]

            elif nums[mid] >= nums[right]:
                left = mid +1

            elif nums[mid] <= nums[right]:
                right = mid -1
            
        return minimum
        