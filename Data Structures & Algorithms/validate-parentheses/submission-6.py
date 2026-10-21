class Solution:
    def isValid(self, s: str) -> bool:

        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        # ([{

        for brace in s:
            
            # open brace -> add to stack
            if brace not in close_to_open:
                stack.append(brace)
            
            # closing brace -> pop from stack -> check if matches close_to_open -> if not False 
            # if s = ) -> stack is empty nothing to match return False
            # if yes: pop from stack
            elif stack == [] or stack[-1] != close_to_open[brace]:
                return False
            else:
                stack.pop()

        if stack == []:
            return True
        return False

# TC: O(n)
# SC: close_to_open -> O(1)
#     stack -> O(n) if s has all open braces where n = len(s)