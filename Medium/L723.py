def candy_crush(board):
    """
    Simulates the Candy Crush game logic, finding and crushing candies and letting them drop.

    Parameters:
        board (List[List[int]]): The game board represented as a 2D list.

    Returns:
        List[List[int]]: The updated game board after candies are crushed and dropped.

    Time Complexity:
        O((m * n)^2): The board is traversed multiple times for candy crushing and dropping until it stabilizes.

    Space Complexity:
        O(m * n): Space used to store coordinates of candies to crush.
    """
    rows, cols = len(board), len(board[0])

    def get_candies_to_crush():
        """Finds all candies that need to be crushed."""
        candies = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 0:
                    continue
                # Check horizontal
                if c + 2 < cols and board[r][c] == board[r][c + 1] == board[r][c + 2]:
                    candies.update({(r, c), (r, c + 1), (r, c + 2)})
                # Check vertical
                if r + 2 < rows and board[r][c] == board[r + 1][c] == board[r + 2][c]:
                    candies.update({(r, c), (r + 1, c), (r + 2, c)})
        return candies

    def eliminate_candies(candies):
        """Eliminates candies by setting their positions to zero."""
        for r, c in candies:
            board[r][c] = 0

    def drop_candies():
        """Simulates gravity by letting candies drop to fill empty spaces."""
        for c in range(cols):
            write_index = rows - 1
            for r in range(rows - 1, -1, -1):
                if board[r][c] != 0:
                    board[write_index][c] = board[r][c]
                    write_index -= 1
            for r in range(write_index, -1, -1):
                board[r][c] = 0

    while True:
        candies_to_crush = get_candies_to_crush()
        if not candies_to_crush:
            break
        eliminate_candies(candies_to_crush)
        drop_candies()

    return board