class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        leftMax, rightMax = 0,0
        soln = 0
        while l < r:
            if height[l] <= height[r]:
                soln += max(0, leftMax - height[l])
                leftMax = max(leftMax, height[l])
                l += 1
            else:
                soln += max(0, rightMax - height[r])
                rightMax = max(rightMax, height[r])
                r -= 1
        return soln