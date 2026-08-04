class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        soln = []
        for i in range(len(nums)):
            product = 1
            for j in range(0, i):
                product *= nums[j]
            for j in range(i+1, len(nums)):
                product *= nums[j]
            soln.append(product)
        return soln
        
        