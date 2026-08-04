class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        soln = [1] * len(nums)
        rightProduct = 1
        for i in range(1, len(nums)):
            soln[i] = soln[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1): #start, stop, step
            rightProduct *= nums[i+1]
            soln[i] *= rightProduct

        return soln