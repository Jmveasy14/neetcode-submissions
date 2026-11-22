class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        if len(nums) == 1 and target == nums[0]:
            return 0
        
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = (left + right) // 2

            #nums=[4,5,6,7,[0,1,2] target=0

            if nums[mid] == target:
                return mid
            #left size
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            #right size
            elif nums[right] >= nums[mid]:
                if nums[right] >= target > nums[mid]:
                    left = mid+1
                else: 
                    right = mid -1

        
        return -1


        