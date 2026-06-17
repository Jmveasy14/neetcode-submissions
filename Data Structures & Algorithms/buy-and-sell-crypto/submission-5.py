class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right =left+1
        curr = 0
        max_profit = 0 
        while right < len(prices):
            if prices[left] < prices[right]:
                curr = prices[right] - prices[left]
                max_profit = max(max_profit,curr)
            
            else:
                left=right
            right+=1
        return max_profit


        