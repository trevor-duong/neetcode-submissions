class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        cars = sorted(zip(position, speed), reverse=True) # sorted lexicographically based on position
        for car in cars:
            if not fleets:
                fleets.append(car)
            else:
                fleet_ahead_time = (target - fleets[-1][0]) / fleets[-1][1]
                cur_car_time = (target - car[0]) / car[1]
                if cur_car_time > fleet_ahead_time: # cur_car takes more time to finish than next fleet --> slower --> new fleet
                    fleets.append(car)
                # else do nothing, no need to append
                    
        return len(fleets)