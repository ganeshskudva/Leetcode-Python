class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_block(block):
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
