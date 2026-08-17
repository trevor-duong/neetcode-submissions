class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        history = self.time_map[key] # list of (timestamp, tuple)
        left, right = 0, len(history) - 1
        soln = -1
        while left <= right:
            mid = (right - left) // 2 + left
            if history[mid][0] <= timestamp:
                soln = mid
                left = mid+1
            elif history[mid][0] > timestamp:
                right = mid-1
                
        if soln == -1:
            return ""
        return history[soln][1]
        
