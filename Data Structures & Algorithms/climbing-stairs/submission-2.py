class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(n):
            
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n <= 0:
                return 0
            if n in memo:
                return memo[n]
            else:
                memo[n] = helper(n-1) + helper(n-2)
                return helper(n-1) + helper(n-2)
        return helper(n)
        

        