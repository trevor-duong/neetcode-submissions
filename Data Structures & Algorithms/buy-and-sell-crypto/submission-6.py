class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running_min = float('inf')
        soln = 0
        for price in prices:
            running_min = min(running_min, price) 
            soln = max(soln, price - running_min)
            print(price, soln)
        return soln