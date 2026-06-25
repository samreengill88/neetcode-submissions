class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        
        maxP = 0

        while sell < len(prices):
            # if buy is less than buy - calc profit
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
            else:
                buy = sell
            sell += 1
        
        return maxP

