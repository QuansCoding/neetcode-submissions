class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # O(n) space
        longest = 0

        for num in numSet: # o(n) time

            #checks if there is a left neighbor in numSet (does not iterate, since checking from hash)
            if (num -1) not in numSet: 
                length = 1

                # Keeps checking next number (does not iterate, since checking from hash)
                while (num+length) in numSet: 
                    length += 1
                longest = max(length,longest) #checks if current length is longer, than the last one.
        return longest