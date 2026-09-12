class MinStack:

    def __init__(self):
        #init 2 stacks (one for normal values, another for min values)
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        # will always append value into stack
        self.stack.append(val)
        # checks min val between stack and min stack val (if not in minStack simply add value)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        #when popping, pops both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] # top value in stack

    def getMin(self) -> int:
        return self.minStack[-1] #returns top value in minStack
        
