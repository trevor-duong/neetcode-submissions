class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        soln = 0
        for token in tokens:
            if token != "+" and token != "-" and token != "*" and token != "/":
                stack.append(int(token))
                continue

            sec = stack.pop()
            first = stack.pop()
            if token == "+":
                soln = first + sec
            elif token == "-":
                soln = first - sec
            elif token == "*":
                soln = first * sec
            elif token == "/":
                soln = int(first / sec)

            stack.append(soln)
        return stack.pop()
