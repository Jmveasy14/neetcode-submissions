class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #this is the index of the last number in nums
        goal = len(nums) -1
        # we are going in reverse
        for i in range(len(nums)-1,-1,-1):
        #if the number before it is greater than equal to the goal, then we know it can get there so we assign that to the goal
            #i is tha index and nums i is the number of jumps
            if i + nums[i] >= goal:
                goal = i
            
        if goal == 0:
            return True

        else:
            return False

