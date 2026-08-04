class MinStack:

    
    def __init__(self):
        self.array = []

    def push(self, val: int) -> None:
        self.array.append(val)

    def pop(self) -> None:
        self.array.pop()

    def top(self) -> int:
        return self.array[len(self.array) - 1]

    def getMin(self) -> int: # O(n) not ideal
        minVal = None
        for val in self.array:
            if minVal == None:
                minVal = val
            if val < minVal:
                minVal = val
        return minVal
        
