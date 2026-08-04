class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Input: Two lists: cars' positions and their associated speeds
        # Computation: Iterate through and group cars to see groupings that exist by 
        # Output: The number of groups that exist by the target location
        #
        # Strategy: we can sort the array in descending order. As we iterate through the 
        # sorted list, we can iterate through the list and calculate the time to reach the target.
        # Everytime we find a car whose calculated time is greater than the max of the current group
        # we have found another group

        res = 0
        carTuples = []
        # Create sorted list of (pos, speed) tuples
        for i, pos in enumerate(position):
            carTuples.append((pos, speed[i]))

        carTuples = sorted(carTuples, reverse=True)
        print(carTuples)

        curGroupTime = 0
        for pos, speed in carTuples:
            time = (target - pos) / speed
            if time > curGroupTime:
                res += 1
                curGroupTime = time


        return res
        