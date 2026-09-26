class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)  # creates a set of the character

        for char in charSet: #
            count = l = 0  # init left and count to 0
            for r in range(len(s)):  # iterates right throughout the string (not set)
                if s[r] == char:  #checks if char and right pointer are same 
                    count += 1
                
                while (r - l + 1) - count > k:
                    if s[l] == char:
                        count -= 1

                    l += 1

                res = max(res, r - l + 1)
        
        return res