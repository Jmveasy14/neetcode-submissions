class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
                return nums[0]        

        def robber(nums):
            if len(nums) == 1:
                return nums[0]       
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])

            for n in range(2,len(nums)):
                loot = nums[n] + dp[n - 2]
                dp[n] = max(dp[n - 1], loot)

            return dp[-1]
        
        return max(robber(nums[1:]), robber(nums[:-1]))
            