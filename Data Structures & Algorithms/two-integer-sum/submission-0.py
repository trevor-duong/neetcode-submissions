class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementsDict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complementsDict:
                return [complementsDict[complement],i]
            complementsDict[num] = i
        return [-1,-1]