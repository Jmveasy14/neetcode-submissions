class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        run = 1
        sequences = []
        if not nums:
            return 0

        if len(nums) == 1:
            return 1
        
        new_nums = set(nums)
        
        for num in new_nums:
            if num -1 not in new_nums:
                run = 1
                curr = num 

                while curr +1 in new_nums:
                    curr +=1
                    run+=1
 
                sequences.append(run)
            

        return max(sequences)