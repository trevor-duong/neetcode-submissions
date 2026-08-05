class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        soln = 0

        while left < right:
            if height[left] <= height[right]:
                soln += max(0, leftMax - height[left])
                leftMax = max(leftMax, height[left])
                left += 1
            else:
                soln += max (0, rightMax - height[right])
                rightMax = max(rightMax, height[right])
                right -= 1
            
        return soln