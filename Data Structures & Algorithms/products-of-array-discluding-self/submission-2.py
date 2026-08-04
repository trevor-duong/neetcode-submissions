class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        soln = [1] * len(nums)
        leftProducts = [1] * len(nums)
        rightProducts = [1] * len(nums)
        
        for i in range(1, len(nums)):
            leftProducts[i] = leftProducts[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1): #start, stop, step
            rightProducts[i] = rightProducts[i+1] * nums[i+1]

        for i in range(len(nums)):
            soln[i] = leftProducts[i] * rightProducts[i]
        return soln