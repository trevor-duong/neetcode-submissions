class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        kernel = [0] * 26
        for char in s1:
            index = ord(char) - ord('a')
            kernel[index] += 1
        
        left, right = 0, len(s1)-1
        window = [0] * 26
        for char in s2[left:right]:
            index = ord(char) - ord('a')
            window[index] += 1

        while right < len(s2):
            window[ord(s2[right]) - ord('a')] += 1
            if kernel == window:
                return True
            left += 1
            right += 1
            window[ord(s2[left-1]) - ord('a')] -= 1

        return False