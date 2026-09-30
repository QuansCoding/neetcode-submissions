class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]  # pairs each car's position and speed

        pairs.sort(reverse=True)  #sort order of position (based on position) in reverse

        stack = []

        for p, s in pairs:  # for each car,
            stack.append((target - p) / s) # push time into stack

            # if new car time is less than or equal to the time before it, it catches up so pop from stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()

        return len(stack)  # return stack size