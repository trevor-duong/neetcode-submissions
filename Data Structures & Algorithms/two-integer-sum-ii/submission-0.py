class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer = 0
        rightPointer = len(numbers) - 1

        while (numbers[leftPointer] + numbers[rightPointer]) != target:
            sumPointers = numbers[leftPointer] + numbers[rightPointer]

            if sumPointers > target:
                rightPointer -= 1
            elif sumPointers < target:
                leftPointer += 1

        
        return [leftPointer+1, rightPointer+1]