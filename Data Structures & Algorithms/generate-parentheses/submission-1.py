class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # We want to explore every single option via a stack. Similar to DFS

        soln = []
        stack = [(0,0,"")] # (opened, closed, string)

        while stack:
            opened, closed, path = stack.pop()
            if len(path) == n*2:
                soln.append(path)

            if closed < opened:
                stack.append((opened, closed+1, path+")"))

            
            if opened < n:
                stack.append((opened+1, closed, path + "("))

    
        return soln
            



        