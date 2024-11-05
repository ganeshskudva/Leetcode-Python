from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3  # Size of the Tic-Tac-Toe board
        rows, cols = [0] * n, [0] * n  # Track row and column sums
        diag1 = diag2 = 0  # Track sums for both diagonals
        
        # Loop through each move, alternating between player A and B
        for index, move in enumerate(moves):
            i, j = move
            sign = 1 if index % 2 == 0 else -1  # Player A is +1, Player B is -1
            
            # Update the row and column for the current move
            rows[i] += sign
            cols[j] += sign
            
            # Update the diagonals if the move is on one of them
            if i == j:
                diag1 += sign  # Main diagonal
            if i + j == n - 1:
                diag2 += sign  # Anti-diagonal
            
            # Check if the current player has won by completing a row, column, or diagonal
            if abs(rows[i]) == n or abs(cols[j]) == n or abs(diag1) == n or abs(diag2) == n:
                return 'A' if sign == 1 else 'B'
        
        # If all cells are filled and no one won, it's a draw
        return "Draw" if len(moves) == (n * n) else 'Pending'

# Time Complexity (TC): O(m), where m is the number of moves.
# - Each move is processed once, updating row, column, and (if applicable) diagonal counts, all of which take constant time.

# Space Complexity (SC): O(1), since we use only a fixed amount of extra space:
# - Three arrays of size 3 (`rows`, `cols`) and two variables (`diag1` and `diag2`), which do not grow with input size.
