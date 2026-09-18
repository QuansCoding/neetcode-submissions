class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop()) # pops the previous two stack values to add
            elif c == "-":
                a,b = stack.pop(), stack.pop()    # pop order matters since you are subtracting
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop()) # order does not matter
            elif c == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))

            else:
                stack.append(int(c)) # adds each number into a stack

        return stack[0] #returns only the first value