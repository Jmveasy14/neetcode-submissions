class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))

        if len(nums) == 1:
            return nums[0]
        
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for n in range(2,len(nums)):
            loot = nums[n] + dp[n - 2]
            dp[n] = max(dp[n-1], loot)
        
        return dp[-1] 

            

        