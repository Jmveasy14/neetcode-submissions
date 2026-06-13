class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #we iterate through the list, for each number, we multiply everything, but that number
        result = [1] * (len(nums))
        prefix = 1
        #use two lists one on the left and one on the right of the num
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result





        