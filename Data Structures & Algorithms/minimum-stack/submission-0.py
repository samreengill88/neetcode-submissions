class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minStack.pop(-1)

    def top(self) -> int:
        # does not remove from the stack, just peep at the last element
        return self.stack[len(self.stack) - 1]

        

    def getMin(self) -> int:
        return min(self.stack)
        
