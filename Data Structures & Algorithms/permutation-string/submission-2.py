class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        kernel = [0] * 26
        for char in s1:
            index = ord(char) - ord('a')
            kernel[index] += 1
        
        left, right = 0, len(s1)
        window = [0] * 26
        for char in s2[left:right]:
            index = ord(char) - ord('a')
            window[index] += 1

        matches = 0
        for i in range(len(kernel)):
            if kernel[i] == window[i]:
                matches += 1
        if matches == 26:
            return True
        while right < len(s2):
            # If the frequency of the char we are adding is currently one 
            # less than the filter, increment matches
            if window[ord(s2[right]) - ord('a')] == kernel[ord(s2[right]) - ord('a')] - 1:
                matches += 1 
            # Else if the frequency of the char we are adding is equal 
            # to that of the filter, decrement matches
            elif window[ord(s2[right]) - ord('a')] == kernel[ord(s2[right]) - ord('a')]:
                matches -= 1
            window[ord(s2[right]) - ord('a')] += 1
            right += 1

            # If the frequency of the char we are removing is currently
            # one more than the filter, increment matches
            if window[ord(s2[left]) - ord('a')] == kernel[ord(s2[left]) - ord('a')] + 1:
                matches += 1 
            # If the frequency of the char we are removing is equal
            # to that of the filter, decrement matches
            elif window[ord(s2[left]) - ord('a')] == kernel[ord(s2[left]) - ord('a')]:
                matches -= 1
            window[ord(s2[left]) - ord('a')] -= 1
            left += 1

            if matches == 26:
                return True

        return False