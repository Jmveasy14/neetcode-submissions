class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        present = set(range((len(nums)+1)))
        missing = 0
        
        for num in present:
            if not num in nums:
                missing = num
        
        return missing
                

         


        