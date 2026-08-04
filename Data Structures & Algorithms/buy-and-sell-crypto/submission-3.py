class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        sellPrice = -1
        maxP = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                buyPrice = min(buyPrice, prices[l])
                sellPrice = prices[r]
                maxP = max(maxP, sellPrice-buyPrice)

            print(buyPrice, sellPrice)
            l += 1
            r += 1
        
        
        return maxP
        