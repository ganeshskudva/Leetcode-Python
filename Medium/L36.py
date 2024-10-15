class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_block(block):
            # Filter out '.' and check if the block has unique values
            block = [num for num in block if num != '.']
            return len(block) == len(set(block))

        # Check rows
        for row in board:
            if not is_valid_block(row):
                return False

        # Check columns
        for col in zip(*board):
            if not is_valid_block(col):
                return False

        # Check 3x3 sub-grids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not is_valid_block(block):
                    return False

        return True

# Time Complexity (TC): 
# - Checking rows takes O(9) for each row, and since there are 9 rows, the total is O(9 * 9) = O(81).
# - Checking columns takes O(9) for each column, and since there are 9 columns, the total is O(81).
# - Checking each 3x3 sub-grid involves processing 9 elements in each of the 9 grids, making it O(81).
# Overall, the time complexity is O(81 + 81 + 81) = O(243), which simplifies to O(1) since the board size is fixed.

# Space Complexity (SC): 
# - The space used by the function is primarily for storing intermediate filtered blocks. Each block contains at most 9 elements.
# - The space complexity for each block is O(9), and since we are checking rows, columns, and sub-grids independently, the total space complexity is O(9), which simplifies to O(1).
