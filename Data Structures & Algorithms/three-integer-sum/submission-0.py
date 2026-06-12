class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        new_nums = sorted(nums)

        for i, a in enumerate(new_nums):
            if i > 0 and a == new_nums[i-1]:
                continue
        
            left = i+1
            right = len(new_nums) -1
        
            while left< right:
                threeSum = a + new_nums[left] + new_nums[right]
                if threeSum > 0:
                    right -=1

                elif threeSum < 0:
                    left+=1
                else:
                    res.append([a,new_nums[left], new_nums[right]])
                    left+=1
                    while new_nums[left] == new_nums[left-1] and left < right:
                        left+=1
        return res
