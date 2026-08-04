class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        soln = 0
        numsSet = set()
        for num in nums:
            numsSet.add(num)
        
        for i, num in enumerate(nums):
            if num - 1 not in numsSet:
                curVal = num
                curLength = 0
                while curVal in numsSet:
                    curLength += 1
                    curVal += 1
                soln = max(soln, curLength)
        
        return soln