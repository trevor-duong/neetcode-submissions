class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                second_op = int(nums.pop())
                first_op = int(nums.pop())
                if token == '+':
                    nums.append(int(first_op + second_op))
                elif token == '-':
                    nums.append(int(first_op - second_op))
                elif token == '*':
                    nums.append(int(first_op * second_op))
                elif token == '/':
                    nums.append(int(first_op / second_op))
            else:
                nums.append(int(token))

        return nums[-1] # Guaranteed by problem definition