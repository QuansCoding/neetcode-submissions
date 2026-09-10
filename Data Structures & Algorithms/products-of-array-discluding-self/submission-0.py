class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)  #len of num is used often
#initailizes an array (length of nums) with each value being 1 (will be used for initial calculation)
        left = [1] * n
        right = [1] * n
#initializes an "empty" array **empty as in filled with 0**(length of nums)
        ans = [0] * n 
        for i in range(1, n):
            # sets current left # to the product of each previous number
            # this means that the left array only has values of products of everything of its index
            left[i] = left[i-1] * nums[i-1] 
# iterates through each index (starting at the 2nd to last value decreasing value and ends at the first value)
        for i in range(n-2,-1,-1):       
            # sets current right number to the product of each previous number
            # means that each value is the array has values of the products of everything else
            right[i] = right[i+1] * nums[i+1]
        for i in range(n):         
#iterates for the length of nums and multiples the left multiples and right multiples together
            ans[i] = left[i] * right[i]
        
        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        