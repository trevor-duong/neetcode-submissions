class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Keep track of how many times each number appears
        soln = []
        frequencyMap = {}
        for num in nums:
            if num not in frequencyMap:
                frequencyMap[num] = 0
            frequencyMap[num] += 1
        sortedNums = sorted(frequencyMap.items(), key = lambda x: x[1], reverse = True) 
        # sorted looks at frequencyMap.items() which is [key, value], key says convert the input x to x[1]
        for i in range(k):
            soln.append(sortedNums[i][0])
        return soln