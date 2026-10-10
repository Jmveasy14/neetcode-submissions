class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l = 0 #buyy
        profit = 0
        r = 1 #sell

        while r < len(prices):

            if prices[r] > prices[l]:

                curr = prices[r] - prices[l]
            
                profit = max(profit,curr)
            
            else:
                l = r
            r+=1

        
        return profit
            


        