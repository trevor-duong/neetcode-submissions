class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in temperatures]
        stack = [] # pair (temp, index)

        for i, temp in enumerate(temperatures):
            while (stack and stack[-1][0] < temp):
                prevTemp, prevIndex = stack.pop()
                res[prevIndex] = i - prevIndex

            stack.append((temp, i))
        
        return res

