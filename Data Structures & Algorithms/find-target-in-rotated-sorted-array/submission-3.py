class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # in a rotated sorted array there are at most two sorted portions, to find the target we can binary search both to find it
        # in O(logn). The first step is to separate the two sorted portions via the finding of a pivot

        # Step 1 find the pivot with binary search

        l, r = 0, len(nums)-1
        
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        print(l)

        def binarySearch(left: int, right: int):
            while left <= right:
                mid = (right + left) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            return -1

        print(pivot)
        searchLeft = binarySearch(0, pivot-1)
        if searchLeft != -1:
            return searchLeft
        
        searchRight = binarySearch(pivot, len(nums) - 1)
        return searchRight

        
                
