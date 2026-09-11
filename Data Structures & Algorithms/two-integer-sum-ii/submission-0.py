class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            currSum = numbers[l] + numbers[r]
        
            if currSum > target: # if currSum is too big, check the next right pointer (moves left)
                r -= 1
            
            elif currSum < target: # currSum is too small, check the next left pointer (moves right)
                l += 1
            
            else:
                return [l+1,r+1]
        
        return[] # if no pairs found, returns empty array
