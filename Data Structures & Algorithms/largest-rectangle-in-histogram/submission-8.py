class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxes = [-1] * len(heights)
        for i, height in enumerate(heights):
            while stack and height < stack[-1][1]:
                left_boundary = -1
                max_tuple = stack.pop()
                if stack:
                    left_boundary = stack[-1][0]
                maxes[max_tuple[0]] = (i - left_boundary - 1) * max_tuple[1]
            stack.append((i,height))
        
        while stack:
            left_boundary = -1
            max_tuple = stack.pop()
            if stack:
                left_boundary = stack[-1][0]
            maxes[max_tuple[0]] = (len(heights) - left_boundary - 1) * max_tuple[1]
        
        return max(maxes)