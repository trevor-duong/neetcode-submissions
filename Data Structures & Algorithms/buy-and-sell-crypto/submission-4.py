class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force: Find every possible buy and sell option and calculate max

        res = 0

        for i, price in enumerate(prices):
            for j in range(i+1, len(prices)):
                res = max(res, prices[j]- prices[i])

        
                
        return res

        