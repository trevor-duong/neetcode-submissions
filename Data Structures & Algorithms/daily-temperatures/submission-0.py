class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force O(n^2)
        res = [0 for _ in temperatures]

        for i, temp in enumerate(temperatures):
            for j in range(i):
                if res[j] != 0:
                    continue
                if temperatures[j] < temperatures[i]:
                    res[j] = i - j
        return res