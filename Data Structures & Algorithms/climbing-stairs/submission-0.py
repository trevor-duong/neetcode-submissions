class Solution:


        
    def climbStairs(self, n: int) -> int:
        lookupTable = {}

        def helper(self, n: int) -> int:

            if n == 0:
                return 1
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            stepsPossibleIfLastWasOne = -1
            if n-1 in lookupTable:
                stepsPossibleIfLastWasOne = helper[n-1]
            else:
                stepsPossibleIfLastWasOne = self.climbStairs(n-1)
                lookupTable[n-1] = stepsPossibleIfLastWasOne
            stepsPossibleIfLastWasTwo = -1
            if n-2 in lookupTable:
                stepsPossibleIfLastWasTwo = helper[n-2]
            else:
                stepsPossibleIfLastWasTwo = self.climbStairs(n-2)
                lookupTable[n-2] = stepsPossibleIfLastWasTwo

            return stepsPossibleIfLastWasOne + stepsPossibleIfLastWasTwo

        return helper(self, n)

        