class TimeMap:

    def __init__(self):
        self.timeMap = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.timeMap:
            return ""
        for val in self.timeMap[key]:
            if val[1] <= timestamp:
                res = val[0]
        return res
