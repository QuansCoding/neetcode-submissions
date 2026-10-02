class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows * cols - 1

        while l <= r:
            m = l + (r - l) // 2  # finds the middle index value
            row, col = m // cols,  m % cols  # finds row and col of middle val
            if target > matrix[row][col]:  # if less than target, move left pointer to mid
                l = m + 1  
            elif target < matrix[row][col]:  # if more than target, move right pointer to mid
                r = m - 1
            else:  # target was found
                return True 
        return False  # target was not found