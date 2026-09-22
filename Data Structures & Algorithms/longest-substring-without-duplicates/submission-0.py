class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:     # when duplicate found
                charSet.remove(s[l])   # removes left most pointer until no more duplicate
                l += 1
            charSet.add(s[r])          # adds right letter into set
            res = max(res, r - l + 1)  # only returns a number
        return res