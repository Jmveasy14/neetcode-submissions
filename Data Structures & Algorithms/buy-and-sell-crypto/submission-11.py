class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1

        max_profit = 0

        while left <= right and right< len(prices):
            #if the buy is less than the sell continue:
            if prices[left] < prices[right] and left != right:
                curr_profit = prices[right] - prices[left]
                max_profit = max(max_profit,curr_profit)
            #otherwise we calculate the profit and then compare with the max profit
            elif prices[right] <= prices[left]:
                left = right
            right += 1
        return max_profit
