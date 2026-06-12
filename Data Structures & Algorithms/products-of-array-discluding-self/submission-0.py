class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        total = [1]* len(nums)
        #for each number, we need to check where it is in the array and
        #then find every other value and multiply them to the total
        #multiply values on the right
        #start with left
        i = 0
        for i in range(len(nums)-1,-1,-1):
            total[i] = left
            left*= nums[i]


                
        #[1,2,4,6]

        
        for i in range(len(nums)):
            total[i] *= right
            right *=nums[i]

        
            

        

        return total
            

        


            



        