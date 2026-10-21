class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = ['+', '-', '*', '/']  
      
        # push numbers in stack
        stack = []
        res = 0

        for token in tokens:
            # token is a digit -> add to stack
            if token not in operators:
                stack.append(int(token))
            
            # token is op -> pop full stack -> apply token -> add result to stack
            else:
                a = stack.pop()
                b = stack.pop()

                if token == '+':
                    res = a + b
                elif token == '-':
                    res = b - a
                elif token == '*':
                    res = a * b
                elif token == '/':
                    res = int(b / a)
                
                stack.append(res)
        
        return stack[-1]