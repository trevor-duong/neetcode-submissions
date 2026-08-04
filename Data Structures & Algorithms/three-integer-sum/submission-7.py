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
            prevLeftVal = None
            prevRightVal = None
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
                    leftPointer += 1
                    rightPointer -= 1
                    if leftVal == prevLeftVal and rightVal == prevRightVal:
                        prevLeftVal = leftVal
                        prevRightVal = rightVal
                        continue
                    soln.append([num,leftVal,rightVal])
                    prevLeftVal = leftVal
                    prevRightVal = rightVal



            prevNum = num
                    

        return soln
            
