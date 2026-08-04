class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i want to keep a lookup table of complements. This way we can iterate 
        # through the list and remember what we have seen, and thus what we are looking for

        # stores complement, index
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target-num],i]
            else:
                seen[num] = i

                

        
        return