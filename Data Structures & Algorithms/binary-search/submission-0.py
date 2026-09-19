class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2  # possible overflow for languages like java (where bit is too large)
            # m = l + (r - l) // 2

            if nums[m] > target:
                r = m-1  # ignores all values right of r
            elif nums[m] < target:
                l = m+1  # ignores all values left of l
            else:
                return m
            
        return -1

            