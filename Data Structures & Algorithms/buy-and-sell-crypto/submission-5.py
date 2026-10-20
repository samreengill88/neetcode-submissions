class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # if buy at 10 sell at 9 -- profit = buy - sell = 1 then update maxProfit
        buy = 0
        sell = 1

        
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)

            # if buy price is higher than sell price -- buy at sell price instead
            if prices[buy] > prices[sell]:
                buy = sell
            sell +=1
        
        return max_profit 
    
    # TC: O(n)
    # SC: O(1)