class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Truley O(n) updates boundaries in O(1) space O(n)
        
        soln = 0
        uniqueNums = set()
        for num in nums: # Construct nums set to iterate through
            uniqueNums.add(num)
        numsLengths = {}

        for num in uniqueNums:
            print(numsLengths)
            lengthLeft = 0
            if num-1 in numsLengths:
                lengthLeft = numsLengths[num-1]
            lengthRight = 0
            if num+1 in numsLengths:
                lengthRight = numsLengths[num+1]
            newLength = lengthLeft + 1 + lengthRight
            #Update boundaries
            numsLengths[num-lengthLeft] = newLength
            numsLengths[num+lengthRight] = newLength
            soln = max(soln, newLength)
        return soln