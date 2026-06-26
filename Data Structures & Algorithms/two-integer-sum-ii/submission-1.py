class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers)-1
        result = []

        while left <= right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                result = [left+1,right+1]
                return result
            
            elif curr_sum > target:
                right-=1
            
            else:
                left+=1

        return result

        