class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we can use two pointers to calculate the areas and find the max
        maxArea = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            thisArea = (r - l) * min(heights[l], heights[r])
            if thisArea > maxArea: 
                maxArea = thisArea

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
                r -= 1
        
        return maxArea
            