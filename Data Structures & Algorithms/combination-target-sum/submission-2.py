class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = set()
        
        def dfs(start,remaining_target,path):
            if remaining_target == 0:
                combos.add(tuple(path))
                return

            if remaining_target < 0:
                return

            for i in range(start,len(nums)):

                dfs(i,remaining_target - nums[i],path + [nums[i]])

        

        dfs(0,target,[])

        return[list(combo) for combo in combos]






            

            

            






        