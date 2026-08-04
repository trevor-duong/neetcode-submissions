class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can either have a max heap of the most frequent of the entire list or a min heap where we are constantly removing the minimum with the
        # higher frequency. After full iteration, the min heap should have the most frequent nums
        # To get frequencies though, we need to do a pass to build a frequency dict

        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1
        print(freqs)
        topKMinHeap = []

        for num, freq in freqs.items():
            print(topKMinHeap)
            if len(topKMinHeap) >= k:
                if freq > topKMinHeap[0][0]:
                    heapq.heappop(topKMinHeap)
                    heapq.heappush(topKMinHeap, (freq, num))
            else:
                heapq.heappush(topKMinHeap, (freq, num))
        
        soln = []
        for num in topKMinHeap:
            soln.append(num[1])
        return soln

