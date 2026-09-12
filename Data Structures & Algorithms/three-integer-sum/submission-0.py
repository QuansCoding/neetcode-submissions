class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #sorts the number list

        for i,a in enumerate(nums):
            if a > 0: # checks if current item is 0
                break
            if i > 0 and a== nums[ i-1]: #if the item is the same as previous
                continue

            l, r = i + 1, len(nums) -1 # intializes left and right pointers
            while l < r:
                threeSums = a + nums[l] + nums[r] # intializes sum of 3
                if threeSums > 0: # if too large move right pointer down
                    r -= 1
                elif threeSums < 0: # if too small move left pointer up
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]]) # appends result
                    l += 1 # moves onto next
                    r -= 1
                    # continues left if curr and prev items are the same
                    while nums[l] == nums[l-1] and l<r: 
                        l += 1
        return res