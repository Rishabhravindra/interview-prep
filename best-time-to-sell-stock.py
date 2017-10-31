# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    
        if len(prices) == 0:
            return 0
        
        min_val = prices[0]
        max_profit = 0         
        
        for price in prices:
            if min_val> price:
                min_val = price
            if price - min_val > max_profit:
                max_profit = price - min_val
        return max_profit                