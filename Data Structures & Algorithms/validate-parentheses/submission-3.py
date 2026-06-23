class Solution:
    def isValid(self, s: str) -> bool:

        # initalize a stack 
        # push all open braces to stack
        # when you get first closing brace - pop from stack, check if it matches its opening brace using closeTo Open dict, if not return False
        # at the end, check if stack empty - return True, o/w return False

        # ex: ([)]

        stack = []
        closeToOpen = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for brace in s:
            # we have opening brace - push to stack
            if brace not in closeToOpen:
                stack.append(brace)
            
            # we have a closing brace - pop from stack, check poped brace if equal to its closing brace
            elif not stack or stack[-1] != closeToOpen[brace]:
                return False
            else:
                # got a matching closing brace
                stack.pop()
        
        # empty stack
        if not stack:
            return True
        else:
            return False

