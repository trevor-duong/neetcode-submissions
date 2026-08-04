class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # With Backtracking there are two cases, one where the 
        soln = []
        path = []

        # In this function, we want to recursively branch into every possible parenthesis combination
        # and add it to the solution
        def backtrack(opened: int, closed: int):
            # Base case, if the string is completed add it to the solution then return
            if len(path) == 2 * n:
                soln.append("".join(path))
                return

            # Case 1, we try and add a opening parenthesis
            if opened < n:
                path.append("(")    # add open parenthesis to current string
                backtrack(opened+1, closed) # explore and add all strings that include this parenthesis
                path.pop() # remove this parenthesis after adding the strings that are possible with it 
                           # so that we may explore the other option
            
            # Case 2: we try and add a closing parenthesis
            if closed < opened:
                path.append(")")
                backtrack(opened, closed + 1)
                path.pop()


        backtrack(0,0)
        return soln

            
        

        