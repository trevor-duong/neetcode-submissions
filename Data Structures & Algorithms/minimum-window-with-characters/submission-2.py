class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # construct filter/kernel
        kernel = defaultdict(int)
        for char in t:
            kernel[char] += 1
        
        # construct window
        matches = 0
        window = defaultdict(int)
        left, right = 0, 0
        shortest_valid_range = (0, float('inf'))
        while right < len(s):
            if s[right] in kernel:

                # if the frequency of the new char is equal 
                # to the kernel's - 1, we have a match      
                if window[s[right]] == kernel[s[right]] - 1: 
                    matches += 1
                

            window[s[right]] += 1
            right += 1

            # if we are valid (matches == num 
            # distinct elements in kernel) shrink the window
            # as much as we can
            while matches == len(kernel):
                # we have a match --> record minimum window
                if right - left < shortest_valid_range[1] - shortest_valid_range[0]:
                    shortest_valid_range = (left, right)

                # we are valid until left is a character
                # in our kernel (ie. s[left] in kernel)
                if s[left] in kernel:

                    if window[s[left]] == kernel[s[left]]:
                        matches -= 1

                window[s[left]] -= 1
                left += 1


        # check so we don't index OOB
        if shortest_valid_range[1] != float('inf'):
            return s[shortest_valid_range[0] : shortest_valid_range[1]]
        return ""
            
                 
            