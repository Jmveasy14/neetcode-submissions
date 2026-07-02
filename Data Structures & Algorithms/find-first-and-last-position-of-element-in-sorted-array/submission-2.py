class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 1 and target in nums:
            return [0,0]

        left = 0
        right = len(nums) -1
        found = []

        while left <= right:
            if nums[left] == target:
                found.append(left)
            if nums[right] == target:
                found.append(right)
            left+=1
            right-=1
            
        if found:
            return [min(found),max(found)]
        else:
            return [-1,-1]


        
        