class Solution:
    def trap(self, height: List[int]) -> int:
        # to calculate the volume at each index, we can use min(maxLeftHeight, maxRightHeight) - h[i]
        # to save space and computation, we can use a two pointer approach. The pointers allow us to know either the 
        # maxLeftHeight or the maxRightHeight at an index which is all we need to calculate the volume

        res = 0
        l, r = 0, len(height)-1

        print(l,r)

        maxHeightLeft = 0
        maxHeightRight = 0
        while l <= r:
            
            volumeAdded = 0
            if maxHeightLeft <= maxHeightRight:
                volumeAdded = maxHeightLeft - height[l]
                maxHeightLeft = max(maxHeightLeft, height[l])
                l += 1
            else:
                volumeAdded = maxHeightRight - height[r]
                maxHeightRight = max(maxHeightRight, height[r])
                r -= 1

            if volumeAdded > 0:
                res += volumeAdded

        return res