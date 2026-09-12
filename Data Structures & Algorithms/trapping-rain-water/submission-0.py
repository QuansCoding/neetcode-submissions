class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: # checks if height is empty
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                #checks prev max and current height
                leftMax = max(leftMax,height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                #checks prev max and current height
                rightMax = max(rightMax,height[r])
                res += rightMax - height[r] 

        return res
