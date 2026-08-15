class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            print(left, mid, right)
            print(row,col)
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False