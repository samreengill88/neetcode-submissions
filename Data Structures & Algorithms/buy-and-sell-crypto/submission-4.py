class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1

        maxP = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            maxP = max(maxP, profit)

            if prices[buy] > prices[sell]:
                buy = sell
            
            sell += 1
        
        return maxP