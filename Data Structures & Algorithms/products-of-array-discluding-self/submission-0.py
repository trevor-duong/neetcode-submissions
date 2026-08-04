class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        soln = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]
            soln.append(product)
        return soln
