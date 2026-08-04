class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # same logic as previous but with a monotonic stack whose invariant is that each
        # element in the stack is a valid fleet

        validFleets = [] # fleet arrival time, 

        carTuples = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        print(carTuples)
        curFleetTime = 0

        for pos, s in carTuples:
            time = (target - pos) / s
            if curFleetTime < time:
                curFleetTime = time
                validFleets.append(time)
        
        return len(validFleets)
