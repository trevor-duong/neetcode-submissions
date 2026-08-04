class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # This solution is alright, it keeps track of the consecutive run lengths at boundaries,
        # But in worst case it is O(n^2) since the updates could be redundant/unnecessarily long
        # Also modifying the dict you are iterating through is bad practice

        numsDict = {}
        if len(nums) == 0:
            return 0
        for num in nums:
            numsDict[num] = 1
        for num, seqLength in numsDict.items():
            print(numsDict)
            if num-1 in numsDict:
                newSeqLength = numsDict[num-1] + numsDict[num]

                numsDict[num + numsDict[num] - 1] = newSeqLength
                numsDict[num - 1 - (numsDict[num-1] - 1)] = newSeqLength
        print(numsDict)

        return max(numsDict.values())
        
        