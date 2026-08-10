class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, 0
        soln = []
        candidates = deque() # contains tuples (index, value)

        # Construct initial deque
        while right < len(nums):

            # remove invalid candidates from deque and append.
            while candidates and candidates[-1][1] < nums[right]:
                candidates.pop()
            candidates.append((right, nums[right]))
            
            # remove elements that have fallen out of our window
            while candidates and candidates[0][0] < left:
                candidates.popleft()
            
            right += 1
            if right >= k:
                soln.append(candidates[0][1])
                left += 1
        
        return soln
        

                

