class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use frequency buckets to avoid using log(k) operations for maintaining a heap 

        # Compute actual frequencies O(n)
        freqDict = {}
        for num in nums:
            if num not in freqDict:
                freqDict[num] = 1
            else:
                freqDict[num] += 1
        print(freqDict)
        # Build frequency buckets and fill them O(n)
        freqBuckets = [[] for _ in range(len(nums) + 1)] # index = frequency, value = nums w/ that frequency
        for num, freq in freqDict.items():
            freqBuckets[freq].append(num)
        
        print(freqBuckets)
        soln = []
        for i in reversed(range(len(freqBuckets))):
            for num in freqBuckets[i]:
                if len(soln) < k:
                    soln.append(num)

        return soln