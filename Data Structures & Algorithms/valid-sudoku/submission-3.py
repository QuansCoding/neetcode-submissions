class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #initializes squares ,column and rows as dictions taking in sets
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        #iterates through each row and column
        for r in range(9):
            for c in range (9):
                # if current index (row and column) is empty (".")
                if board[r][c] == ".":
                    continue

                # checks if current index is already in...
                #   rows index or cols index
                #   within square 2d Array index
                if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares [(r // 3), (c // 3)]): 
                    return False
                
                #otherwise adds current digit to all 3 sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3),(c // 3)].add (board[r][c]) # keeps in 3x3 box

        #if full compiled and no False return, returns true
        return True