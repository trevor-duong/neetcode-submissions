class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # the brute force is to check every possible substring 
        # and record the most frequent character in the substring
        # the substring is valid if the length of the substring 
        # minus the highest frequency is <= k
        res = 0
        for i in range(len(s)):
            freqs = {} # map for frequency of each char in every substring starting at i
            maxFreq = 0
            for j in range(i, len(s)): # The content of this block is ran for each substring in range (i,j)
                freqs[s[j]] = 1 + freqs.get(s[j], 0)
                maxFreq = max(maxFreq, freqs[s[j]])
                if (j - i - maxFreq + 1 <= k):
                    res = max(res, j-i + 1)
                print(i,j)

        return res