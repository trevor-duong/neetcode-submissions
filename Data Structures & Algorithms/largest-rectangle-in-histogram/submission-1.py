class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Brute force solution: check every single rectangle that can be formed and track the max
        # O(n^2) since iterating through heights for each element in heights
        res = 0

        for i, height in enumerate(heights):
            width = 1
            j = i + 1
            while j < len(heights) and heights[j] >= height:
                width += 1
                j += 1

            j = i - 1
            while j >= 0 and heights[j] >= height:
                width += 1
                j -= 1

            area = width * height
            res = max(area, res)

            print(i, width)


        return res
