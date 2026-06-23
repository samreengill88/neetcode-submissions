class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # push all nos to stack
        # if its an op -> pop a and b from stack and apply op 
        # push the res in stack

        stack  = []
        ops = ['+', '-', '*', '/']
        res = 0

        for token in tokens:
            if token not in ops:
                # int(token): since number is a string in tokens
                stack.append(int(token))

            # know token is one of the operators
            else:
                a = stack.pop()
                b = stack.pop()

                if token == '+':
                    res = a + b
                elif token == '-':
                    res = b - a
                elif token == '*':
                    res = a * b
                else:
                    res = int(b / a)

                stack.append(res)
        
        return stack[-1]
        