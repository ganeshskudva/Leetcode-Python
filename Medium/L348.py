class TicTacToe:

    def __init__(self, n: int):
        # Initialize the game board with n rows and n columns.
        # `self.rows` keeps track of the sum of moves in each row.
        self.rows = [0] * n

        # `self.cols` keeps track of the sum of moves in each column.
        self.cols = [0] * n

        # `self.diag` keeps track of the sum of moves in the main diagonal (top-left to bottom-right).
        self.diag = 0

        # `self.anti_diag` keeps track of the sum of moves in the anti-diagonal (top-right to bottom-left).
        self.anti_diag = 0

        # `self.size` stores the size of the board (n x n).
        self.size = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Make a move by a player. The method updates the game state and checks if a player has won.
        :param row: Row index of the move
        :param col: Column index of the move
        :param player: 1 for player 1, -1 for player 2
        :return: Returns 1 if player 1 wins, -1 if player 2 wins, or 0 if no one has won yet.
        """

        # Determine what value to add to the tracking arrays based on the player.
        # Player 1 adds +1, Player 2 adds -1.
        to_add = 1 if player == 1 else -1

        # Update the row sum for the current move.
        self.rows[row] += to_add

        # Update the column sum for the current move.
        self.cols[col] += to_add

        # If the move is made on the main diagonal (i.e., row == col),
        # update the diagonal sum.
        if row == col:
            self.diag += to_add

        # If the move is made on the anti-diagonal (i.e., row + col == n - 1),
        # update the anti-diagonal sum.
        if col + row == self.size - 1:
            self.anti_diag += to_add

        # Check if the current player has won:
        # A player wins if the absolute value of any row, column, diagonal, or anti-diagonal
        # equals the size of the board (which means that all elements in that row/column/diagonal
        # have been claimed by the same player).
        if abs(self.rows[row]) == self.size or abs(self.cols[col]) == self.size or \
           abs(self.diag) == self.size or abs(self.anti_diag) == self.size:
            return player

        # If no one has won yet, return 0.
        return 0

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)