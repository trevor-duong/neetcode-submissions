class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # The goal is to find the left and right boundaries for each 
        # height in list, then find the max
        # To find the boundaries in O(n) we can use a monotonically 
        # Increasing stack. This works because we need to keep track of 
        # all heights that have yet to be assigned a right boundary 

        res = -1
        boundaries = [[-1,-1] for _ in heights]
        stack = []

        for i, height in enumerate(heights):
            # Case 1: height > top of stack
            if not stack or height > heights[stack[-1]]:
                boundaries[i][0] = i

            elif height < heights[stack[-1]]:
                lastPopped = -1
                while stack and heights[stack[-1]] > height:
                    lastPopped = stack.pop()
                    boundaries[lastPopped][1] = i
                boundaries[i][0] = boundaries[lastPopped][0]
                if stack and heights[stack[-1]] == height:
                    boundaries[i][0] = boundaries[stack[-1]][0]
            
            elif height == heights[stack[-1]]:
                boundaries[i][0] = boundaries[stack[-1]][0]

            stack.append(i)

        # flush remaining elements from stack and assign boundaries
        while stack:
            i = stack.pop()
            boundaries[i][1] = len(heights)

        # Use boundaries to calculate max
        for i, height in enumerate(heights):
            area = (boundaries[i][1] - boundaries[i][0]) * height
            res = max(area, res)

        print(boundaries)
        print(stack)
        return res