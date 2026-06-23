class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == '+':
                num2 = stack.pop(-1)
                num1 = stack.pop(-1)
                stack.append(num1 + num2)

            elif tokens[i] == '-':
                num2 = stack.pop(-1)
                num1 = stack.pop(-1)
                stack.append(num1 - num2)

            elif tokens[i] == '*':
                num2 = stack.pop(-1)
                num1 = stack.pop(-1)
                stack.append(num1 * num2)

            elif tokens[i] == '/':
                num2 = stack.pop(-1)
                num1 = stack.pop(-1)
                stack.append(int(num1 / num2))
            
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]
    
    
