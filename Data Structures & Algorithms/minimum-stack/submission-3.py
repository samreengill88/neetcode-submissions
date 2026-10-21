class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        # update min_stack
        if self.min_stack == []:
            min_val = val
        else:
            min_val = min(self.min_stack[-1], val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        if self.stack == []:
            return 

        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
