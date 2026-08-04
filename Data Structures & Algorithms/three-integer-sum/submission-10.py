class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        soln = []
        nums.sort()
        for i, target in enumerate(nums):

            # prevent duplicates
            if i > 0 and target == nums[i-1]:
                continue

            # pointers for 2 pointer approach 
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[left] + nums[right]
                if sum == -target:
                    soln.append([target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < len(nums) and nums[left] == nums[left-1]:
                        left += 1
                    while right >= 0 and nums[right] == nums[right+1]:
                        right -= 1
                
                if sum < -target:
                    left += 1
                    while left < len(nums) and nums[left] == nums[left-1]:
                        left += 1

                if sum > -target:
                    right -= 1
                    while right >= 0 and nums[right] == nums[right+1]:
                        right -=1
        return soln
                