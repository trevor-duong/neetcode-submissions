class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the brute force solution is to iterate through each pile and check each different possible eating rate
        # returning the minimum such that it is less than h

        res = -1
        rate = max(piles) // 2
        left = 1
        right = max(piles)

        while left <= right:
            rate = (right-left) // 2 + left
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
            print(rate, hours)
            if hours > h: # this means our rate is too small, look for a bigger rate
                left = rate + 1
            elif hours <= h: # our rate is big, lets look for a smaller one
                res = rate
                right = rate - 1

        return res
            

        return -1