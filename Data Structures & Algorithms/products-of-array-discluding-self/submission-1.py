class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        total =[1] * len(nums)

        #iterate backwards getting all values on the right of index
        for i in range(len(nums)-1,-1,-1):
            total[i] *= right

            right*=nums[i]

        for i in range(len(nums)):
            total[i] *= left

            left *= nums[i]

        return total