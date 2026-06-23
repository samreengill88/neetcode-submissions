class Solution:
    def isValid(self, s: str) -> bool:
        order_braces = {')': '(',
                        ']': '[',
                        '}': '{'
                        }
        # put open brackets in stack
        stack = []
        
        for bracket in s:
            # if it's opening bracket (i.e., if not in order_braces),  add it to stack 
            if bracket not in order_braces:  # its opening bracket
                stack.append(bracket)
            
            # know it's a closing brace
            else:
#                # check if stack is not empty and last element of stack matches order_braces[bracket]
                if stack and order_braces[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False
                