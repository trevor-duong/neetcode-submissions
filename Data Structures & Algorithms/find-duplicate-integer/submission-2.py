class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0 # indices

        # get index where fast and slow pointer meet within cycle. (duplicates 
        # create a cycle via returning to the same position multiple times)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Cycle beginning is the duplicate number. fast and slow are at k elements away from cycle beginning. L is num jumps until cycle       
        # beginning
        # Via algebra... 2(L+k) = L + k + mC where L = num jumps from cycle beginning, and k = steps into cycle, 
        # and C = cycle length, and m equal cycle iterations
        # L = mC - k
        # L = (m-1)C + (C - k) where (m-1)C is just full cycles, so L = (C-k). To find duplicate, we can just find when L = (C - k), and we
        # already have (C - k) from the previous loop
        L = 0
        while L != slow:
            L = nums[L]
            slow = nums[slow]
         
        return L