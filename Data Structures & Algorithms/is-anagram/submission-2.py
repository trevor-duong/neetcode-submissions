class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCharCounts = {}
        tCharCounts = {}
        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            if sChar in sCharCounts:
                sCharCounts[sChar] += 1
            else:
                sCharCounts[sChar] = 1
            if tChar in tCharCounts:
                tCharCounts[tChar] += 1
            else:
                tCharCounts[tChar] = 1
        
        return sCharCounts == tCharCounts