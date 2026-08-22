class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): # ensure nums1 is the larger of the arrays to ensure we aren't overdrawing from nums2
            nums1, nums2 = nums2, nums1

        left, right = 0, len(nums1) # binary search over k, the number of elements to include in the left partition from nums1
        while left <= right: # want to converge on proper partitioning of elements from nums1 and nums2
            k = (right - left) // 2 + left # number of elements taken from nums1
            j = (len(nums1) + len(nums2) + 1) // 2 - k # number of elements taken from nums2

            # boundary elements from both lists
            left1, right1, left2, right2 = -1, -1, -1, -1

            # Set boundary elements for nums1 for this particular partition
            if k == 0:
                left1 = float('-inf')
            else:
                left1 = nums1[k-1]
            if k == len(nums1):
                right1 = float('inf')
            else:
                right1 = nums1[k]

            # Set boundary elements for nums2 for this particular partition
            if j == 0:
                left2 = float('-inf')
            else:
                left2 = nums2[j-1]
            if j == len(nums2):
                right2 = float('inf')
            else:
                right2 = nums2[j]
            
            # Boundary checks + binary search recursion
            if left1 > right2: 
                # left1 is too big, we need to take more elements from nums2 --> decrease k
                right = k-1
            elif left2 > right1:
                # left2 is too big, we need to take more elements from nums1 --> increase k
                left = k+1
            else:
                # Everything is valid, the k we have is correct. Compute median from these valid boundaries
                if (len(nums1) + len(nums2)) % 2 == 1: # odd
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2




        