class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # to solve this, we can use a sliding window approach looking at the current valid substring, keeping track of the
        # max length that we find. If we encounter a char that is in the window, increment the left pointer until the 
        # substring is valid. This ensures all valid max length substrings are recorded
        res = 0
        l = 0
        charsSeen = set()

        for r, char in enumerate(s):
            while char in charsSeen and l < r:
                charsSeen.remove(s[l])
                l += 1
            charsSeen.add(char)
            res = max(res, len(charsSeen))
            print(charsSeen)

        return res
