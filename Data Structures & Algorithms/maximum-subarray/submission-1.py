class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        res = nums[0]
        for n in nums[1:]:
            tmp = curr_max + n
            curr_max = max(n,tmp)

            res = max(res,curr_max)
        
        return res
        