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
            # brute force
        # for val in self.timeMap[key]:
        #     if val[1] <= timestamp:
        #         res = val[0]
        listOfVals = self.timeMap[key]
        l, r = 0, len(listOfVals) - 1

        while l <= r:
            m = (l + r) // 2

            if timestamp >= listOfVals[m][1]:
                l = m + 1
                res = listOfVals[m][0]
            
            elif timestamp < listOfVals[m][1]:
                r = m - 1
            
            
        return res
