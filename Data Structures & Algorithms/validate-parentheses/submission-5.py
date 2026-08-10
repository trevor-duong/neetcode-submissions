class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {')': '(', '}': '{', ']': '[' }
        history = []

        for char in s:
            if char == ')' or char == '}' or char == ']':
                if not history or history.pop() != mappings[char]:
                    return False
            else:
                history.append(char)
                
            print(history)

        if history:
            return False
            
        return True
