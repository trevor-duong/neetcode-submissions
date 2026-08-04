class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Max heap approach since sorting the frequency Map is kinda slow
        soln = []
        frequencyMap = {}
        for num in nums:
            if num not in frequencyMap:
                frequencyMap[num] = 0
            frequencyMap[num] += 1
        
        maxHeap = [(-value,key) for key,value in frequencyMap.items()]
        heapq.heapify(maxHeap)
        for _ in range(k):
            soln.append(heapq.heappop(maxHeap)[1])
        return soln