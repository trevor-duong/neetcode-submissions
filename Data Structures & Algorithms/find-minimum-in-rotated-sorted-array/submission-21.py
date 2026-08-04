class Solution:
    def findMin(self, nums: List[int]) -> int:
        # to find the min intuitively, we can use a binary search algorithm
        # when we have low, mid, high, consider the different cases (There are 2 options for mids relation
        # to low and 2 options for mids relation to high, so there are 2*2 = 4 possible cases)
        # Base case: if nums[(mid+1)%len(nums)] = nums[mid] + 1 and 
        # nums[mid-1] = len(nums) + nums[mid] - 1 return mid
        # Case 1: mid > high and mid < low: [3,4,5,6,1,2]
        #   Then the minimum is to the right so binary search to the right
        # Case 2: mid < high and mid < low: [6,1,2,3,4,5]
        #   Then the minimum is to the left so binary search to the left
        # Case 3: mid > high and mid > low: [2,3,4,5,6,1]
        #   Then the minimum is to the right so binary search to the right
        # Case 4: mid < high and mid > low: [1,2,3,4,5,6]
        #   Then the minimum is to the left so binary search to the left

        left = 0
        right = len(nums) - 1
        mid = (right - left) // 2 + left

        if len(nums) == 1:
            return nums[0]

        while left <= right:
            mid = (right - left) // 2 + left
            if nums[(mid+1)%(len(nums))] > nums[mid] and nums[mid-1] > nums[mid]:
                return nums[mid]
            print("Num to the right of mid:", nums[(mid+1)%len(nums)])
            print("Num to the left of mid:", nums[mid-1])
            print(left,mid,right)
            if nums[mid] >= nums[right] and nums[mid] <= nums[left]:
                print("Case 1")
                left = mid + 1
            elif nums[mid] <= nums[right] and nums[mid] <= nums[left]:
                print("Case 2")
                right = mid - 1
            elif nums[mid] >= nums[right] and nums[mid] >= nums[left]:
                print("Case 3")
                left = mid + 1
            elif nums[mid] <= nums[right] and nums[mid] >= nums[left]:
                print("Case 4")
                right = mid - 1

        return -1




