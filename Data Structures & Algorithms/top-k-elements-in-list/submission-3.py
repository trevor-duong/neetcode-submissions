class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket approach for O(n) time complexity
        soln = []
        frequencyDict = {}
        for num in nums:
            if num not in frequencyDict:
                frequencyDict[num] = 0
            frequencyDict[num] += 1
        
        # freqBuckets is a list of length len(nums)+1 where each index is a bucket of nums that have that frequency
        freqBuckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in frequencyDict.items():
            freqBuckets[freq].append(num)
        
        elementsCounted = 0
        for bucket in reversed(freqBuckets):
            for element in bucket:
                if elementsCounted < k:
                    soln.append(element)
                    elementsCounted += 1
                    
        return soln

        #Runtime analysis
        # Finding the frequencies is O(n). In the worst case frequencyDict is n long 
        # so filling the freqBuckets is worst case O(n). Iterating through the freqBuckets is O(k) 
        # but in the worst case O(n). THus the runtime is O(n + n + n) = O(n)


