class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute force. We look at every char and see how far we can go before we find a duplicate. Return the max

        res = 0

        for i, start in enumerate(s):
            curLength = 0
            charsSeen = set()
            for char in s[i:]:
                if char in charsSeen:
                    break
                charsSeen.add(char)
                curLength += 1
                res = max(res,curLength)
                
        return res