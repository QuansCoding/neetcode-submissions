class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r: # iterates entire string
            while l < r and not s[l].isalnum(): # moves until left pointer until l is valid letter
                l += 1
            while l < r and not s[r].isalnum(): # moves right pointer until r is a valid letter
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True

