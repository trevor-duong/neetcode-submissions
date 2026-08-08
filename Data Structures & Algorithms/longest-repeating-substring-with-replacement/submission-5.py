class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        max_counts = 0
        left = 0
        soln = 0
        for right, char in enumerate(s):
            counts[char] += 1
            max_counts = max(max_counts, counts[char])
            if (right - left + 1) - max_counts > k:
                counts[s[left]] -= 1
                left += 1
            soln = max(soln, right - left + 1)
        return soln