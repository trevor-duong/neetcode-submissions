class MinStack:

    
    def __init__(self):
        self.array = []
        self.mins = []

    def push(self, val: int) -> None:
        if len(self.mins) == 0:
            self.mins.append(val)
        elif val > self.mins[-1]:
            self.mins.append(self.mins[-1])
        else:
            self.mins.append(val)

        self.array.append(val)

    def pop(self) -> None:
        self.mins.pop()
        self.array.pop()

    def top(self) -> int:
        return self.array[len(self.array) - 1]

    def getMin(self) -> int: # O(n) not ideal
        return self.mins[-1]
        
