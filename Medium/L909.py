from collections import deque

def snakes_and_ladders(board):
    """
    This function solves the Snakes and Ladders game using a BFS approach.
    
    The game board is represented by a 2D grid, where some cells may contain snakes or ladders.
    The goal is to find the minimum number of moves to reach the last cell (n * n) from the first cell (1).
    
    Args:
    board: List[List[int]] - A 2D list representing the board. 
            -1 means no snake or ladder on that cell. 
            Any other positive number means that cell has a snake or ladder leading to another cell.
    
    Returns:
    int - The minimum number of moves to reach the last cell (n * n), or -1 if it is not possible.
    """
    
    # Closure function to get the value from the board at a given 1D position 'num'.
    # Converts the 1D position into 2D coordinates based on the zigzag structure of the board.
    def get_board_value(num):
        """
        Convert a 1D board index into 2D coordinates based on the snakes and ladders board layout.
        The board alternates direction per row (zigzag pattern).
        
        Args:
        num: int - The 1D board index (1-based).
        
        Returns:
        int - The value of the board at the calculated 2D position.
        """
        n = len(board)  # Size of the board (n x n)
        r = (num - 1) // n  # Determine the row number (0-indexed)
        
        # Determine the row's x-coordinate from the bottom to the top
        x = n - 1 - r
        
        # Determine the y-coordinate, alternating direction based on row parity
        if r % 2 == 0:
            y = (num - 1) % n  # Even rows go left to right
        else:
            y = n - 1 - (num - 1) % n  # Odd rows go right to left
        
        return board[x][y]  # Return the value at the (x, y) coordinates on the board

    n = len(board)  # Size of the board (n x n)
    visited = [False] * (n * n + 1)  # Array to track visited cells (1-based indexing)
    q = deque([1])  # BFS queue initialized with the starting position 1
    moves = 0  # Counter to track the number of moves

    while q:
        size = len(q)  # Process all positions in the current layer (all cells reachable in 'moves' steps)
        
        for _ in range(size):
            num = q.popleft()  # Get the next position from the queue
            
            # If this number has already been visited, skip it
            if visited[num]:
                continue
            
            # Mark this number as visited
            visited[num] = True

            # If we've reached the last cell (n * n), return the number of moves taken
            if num == n * n:
                return moves

            # Explore all possible moves by rolling a dice (1 to 6 steps)
            for i in range(1, 7):
                next_num = num + i  # Calculate the next position by adding dice roll to the current number
                
                # If the next position is within the board's limits
                if next_num <= n * n:
                    # Check if the next position has a snake or ladder
                    val = get_board_value(next_num)
                    if val != -1:  # If there's a snake/ladder, update next_num to the destination
                        next_num = val
                    
                    # If the destination cell hasn't been visited yet, add it to the queue
                    if not visited[next_num]:
                        q.append(next_num)
        
        # Increment the move counter after processing all positions in the current layer
        moves += 1

    # If we never reach the final cell, return -1
    return -1


# Time Complexity (TC):
# The maximum number of positions we can explore is n^2, where 'n' is the board size.
# For each position, we can roll the dice up to 6 times (constant time operation).
# Therefore, the time complexity is O(n^2) because we process each position once, 
# and for each position, we perform O(1) work (dice rolls and board value lookup).
#
# Space Complexity (SC):
# The space complexity is O(n^2) because:
# - The 'visited' array stores n^2 boolean values (one for each cell).
# - The 'deque' queue can hold up to n^2 positions in the worst case, 
#   although in practice it will hold fewer due to the BFS layer-by-layer approach.
# - The closure 'get_board_value' runs in constant space as it only processes local variables.
#
# Thus, the overall space complexity is O(n^2).
