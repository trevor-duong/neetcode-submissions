class Solution:
    def trap(self, height: List[int]) -> int:
        # To calculate the water that can be stored at a certain index, we can use the equation
        # min(maxLeftHeight, maxRightHeight) - height[i] where maxLeftHeight is the highest 
        # elevation to the left of the index and maxRightHeight is to the right. We want it so 
        # that the this calculation is always positive (can't have negative water filled)
    
        res = 0
        maxLeftHeights = [0 for _ in height]
        maxRightHeights = [0 for _ in height]

        curMaxHeight = 0
        for i, h in enumerate(height):
            maxLeftHeights[i] = curMaxHeight
            curMaxHeight = max(h, curMaxHeight)

        curMaxHeight=0
        for i, h in enumerate(reversed(height)):
            originalIndex = len(height) - 1 - i
            maxRightHeights[originalIndex] = curMaxHeight
            curMaxHeight = max(h, curMaxHeight)


        for i, h in enumerate(height):
            volumeAdded = min(maxLeftHeights[i], maxRightHeights[i]) - height[i]
            if volumeAdded > 0:
                res += volumeAdded
                
        return res
        
