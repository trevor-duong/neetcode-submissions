class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # input: sorted array ascending intergers (nums) and a target
        # output: return the index of the target within nums
        # To solve this recursively, we constantly split the list into two
        # with the range being narrowed to include the target

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = r - l // 2
            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                l = mid + 1
            
            elif target < nums[mid]:
                r = mid - 1

        return -1

            

        

        

