class Solution:
    def isPalindrome(self, s: str) -> bool:
        bare = "" #initialize empty string
        
        for char in s:
            if char.isalnum():
                bare += char.lower()
            
        return bare == bare[::-1]

