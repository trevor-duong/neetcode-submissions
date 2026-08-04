class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # To do this problem, we can first find the row in which the target is located with binary search
        # then within this row we can just search the row with binary search to find whether the target appears

        l, r = 0, len(matrix)-1

        row = -1
        while l <= r:
            mid = (r-l) // 2 + l
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid
                break
            
            elif target > matrix[mid][-1]:
                l = mid + 1

            elif target < matrix[mid][0]:
                r = mid - 1


        l, r = 0, len(matrix[row]) - 1
        print(l,r)
        while l <= r:
            mid = (r-l) // 2 + l

            print(mid)
            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1

        return False