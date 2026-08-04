class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force: Find every possible buy and sell option and calculate max

        res = 0
        buyPrice = prices[0]
        for i, price in enumerate(prices):
            res = max(res, price - buyPrice)
            if price <= buyPrice:
                buyPrice = price
            

        
                
        return res

        