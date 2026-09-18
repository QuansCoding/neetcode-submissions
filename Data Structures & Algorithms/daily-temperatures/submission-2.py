class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # creates a res the length of temperatures
        stack = [] # stack pairs : [temp, index] days that haven't found a 

        for i, temp in enumerate(temperatures): # enumerates temperatures
        # while stack is NOT empty and the curr temp is warmer than top of stack
            while stack and temp > stack[-1][0]: 
                stackT, stackInd = stack.pop() # pops the top element
                res[stackInd] = i - stackInd # appends current stack index
            stack.append((temp, i))
        return res
