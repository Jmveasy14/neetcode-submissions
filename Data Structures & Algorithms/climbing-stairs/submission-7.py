class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(num):
            if num == 1:
                return 1
            
            if num == 2:
                return 2
            
            if num in memo:
                return memo[num]
            

            memo[num] = (climb(num -2 ) + climb(num-1))

            return memo[num]

        return climb(n)
        
