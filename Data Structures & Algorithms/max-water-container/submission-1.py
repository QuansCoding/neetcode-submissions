class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1 #initailizes pointers
        res = 0

        while l < r: 
            area = min(heights[l], heights[r]) * (r - l) # finds the current area
            res = max(res, area)            # if curr area is higher than old res replaces with curr
            if heights[l] <= heights[r]:    # if the left is less than right
                l += 1      # move left (+)
            else:
                r -= 1      # move right (-)
        return res