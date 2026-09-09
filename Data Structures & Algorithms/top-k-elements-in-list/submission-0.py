class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #creates a dictionary
        for num in nums:
            # for each num in nums, sets num as key and increases count by 1 (sets value at 0 if no num)
            count[num] = 1 + count.get(num,0)

        stack = [] #empty stack

        #for each item in count, using num (key) and cnt (value)
        for num, cnt in count.items():
            stack.append([cnt,num])
        stack.sort() # sorts stack

        res = [] # empty result array
        while len(res)<k:
            res.append(stack.pop()[1]) #adds to result stack highest freq (key = num)
        return res
