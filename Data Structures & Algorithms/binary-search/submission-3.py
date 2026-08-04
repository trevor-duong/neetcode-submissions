class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # naive solution: 
        # input: sorted array ascending intergers (nums) and a target
        # output: return the index of the target within nums

        for i, num in enumerate(nums):
            if num == target:
                return i
                
        return -1

