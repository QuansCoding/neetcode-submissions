class MinStack:

    def __init__(self):
        #init 2 stacks (one for normal values, another for min values)
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        # will always append value into stack
        self.stack.append(val)
        # checks if minStack is empty or curr val is less than minVal
        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1]) #adds prev minVal as curr minVal

    def pop(self) -> None:
        #when popping, pops both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] # top value in stack

    def getMin(self) -> int:
        return self.minStack[-1] #returns top value in minStack
        
