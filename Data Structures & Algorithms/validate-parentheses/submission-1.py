class Solution:
    def isValid(self, s: str) -> bool:
        #creates a mapping of all brackets
        mapping = {
            "}" : "{",
            ")" : "(",
            "]" : "[",
        }
        stk = []    # empty stack

        for b in s: # iterates through stack
            # checks if the bracket is in mapping
            if b in mapping:
                #if its also in stack and last closed bracket is the same as current,
                if stk and stk[-1] == mapping[b]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(b)
        # returns true if there are not values left in stack and false otherwise.
        return True if not stk else False 