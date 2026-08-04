class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we want to know what numbers we have seen before so that we can check consecutivity. 
        # we can use a hash set for this, this takes care of duplicates
        # Once we have populated hour hash set we can iterate through and check if num - 1 is contained in the set
        # There is only one number that is equal to num + 1, so no overcounting. Additionally no duplicates in set so no overcounting as well
        # this solution incorrectl

        numsDict = {}
        if len(nums) == 0:
            return 0
        for num in nums:
            numsDict[num] = 1
        for num, seqLength in numsDict.items():
            print(numsDict)
            if num-1 in numsDict:
                newSeqLength = numsDict[num-1] + numsDict[num]
                for i in range(numsDict[num]):
                    numsDict[num+i] = newSeqLength
                for i in range(numsDict[num-1]):
                    numsDict[num-1-i] = newSeqLength
                numsDict[num] = numsDict[num-1]
        print(numsDict)

        return max(numsDict.values())
        
        