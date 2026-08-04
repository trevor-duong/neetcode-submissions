class Solution:
    # Three sum is the same as 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        print(sortedNums)
        soln = []
        prevNum = None
        for i, num in enumerate(sortedNums[:-2]):
            if num == prevNum:
                continue
            leftPointer = i + 1
            rightPointer = len(sortedNums) - 1
            while leftPointer < rightPointer:
                leftVal = sortedNums[leftPointer]
                rightVal = sortedNums[rightPointer]
                twoSum = leftVal + rightVal
                if twoSum < -num:
                    print("twoSum <", num, leftVal, rightVal) 
                    leftPointer += 1
                elif twoSum > -num:
                    print("twoSum >", num, leftVal, rightVal) 
                    rightPointer -= 1
                else:
                    # skip all duplicates on the left
                    while leftPointer < rightPointer and sortedNums[leftPointer] == leftVal:
                        leftPointer += 1
                    # skip all duplicates on the right
                    while leftPointer < rightPointer and sortedNums[rightPointer] == rightVal:
                        rightPointer -= 1
                    soln.append([num,leftVal,rightVal])

            prevNum = num
                    

        return soln
            
