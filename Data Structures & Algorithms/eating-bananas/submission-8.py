class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        soln = -1
        while left <= right:
            mid = (right - left) // 2 + left
            candidate_hours = 0
            for pile in piles:
                candidate_hours += math.ceil(pile / mid)
            if candidate_hours <= h:
                soln = mid
                right = mid - 1
            elif candidate_hours > h:
                left = mid + 1
        return soln
                