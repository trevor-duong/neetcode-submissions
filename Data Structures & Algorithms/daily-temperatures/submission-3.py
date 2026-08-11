class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        soln = [0] * len(temperatures)
        unresolved_days = []
        for i, temp in enumerate(temperatures):
            while unresolved_days and temp > unresolved_days[-1][1]:
                soln[unresolved_days[-1][0]] = i - unresolved_days[-1][0]
                unresolved_days.pop()
            unresolved_days.append((i, temp))

        return soln