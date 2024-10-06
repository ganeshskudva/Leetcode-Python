class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Step 1: Base case to handle if the board is empty or too small to have enclosed regions.
        # If the board is empty or if there are fewer than 3 rows or columns, return immediately.
        if not len(board) or not len(board[0]):
            return
        if len(board) < 3 or len(board[0]) < 3:
            return

        # Step 2: Get the dimensions of the board (m = number of rows, n = number of columns).
        m, n = len(board), len(board[0])

        # Define possible movement directions for DFS (right, down, left, up).
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # Step 3: Helper function to check if a cell (x, y) is within bounds and contains 'O'.
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and board[x][y] == 'O'

        # Step 4: DFS function to traverse and mark all 'O's connected to the borders.
        # It marks connected 'O's with '*' so they won't be flipped to 'X'.
        def solve(x, y):
            # If the cell is out of bounds or does not contain 'O', return.
            if not is_valid(x, y):
                return
            
            # Mark the current 'O' cell as visited by changing it to '*'.
            board[x][y] = '*'
            
            # Explore all four neighboring cells (right, down, left, up).
            for dx, dy in dirs:
                solve(x + dx, y + dy)

        # Step 5: Traverse the borders of the board (first and last columns of all rows, first and last rows of all columns).
        # This identifies the 'O's that are connected to the borders and won't be flipped.
        for i in range(m):
            if board[i][0] == 'O':
                solve(i, 0)  # Check the left border.
            if board[i][n - 1] == 'O':
                solve(i, n - 1)  # Check the right border.

        for j in range(1, n - 1):
            if board[0][j] == 'O':
                solve(0, j)  # Check the top border.
            if board[m - 1][j] == 'O':
                solve(m - 1, j)  # Check the bottom border.

        # Step 6: Traverse the entire board again to:
        # - Flip all remaining 'O's (that are not connected to the border) to 'X'.
        # - Convert '*' (border-connected 'O's) back to 'O'.
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # Flip enclosed 'O' to 'X'.
                if board[i][j] == '*':
                    board[i][j] = 'O'  # Revert '*' back to 'O'.

# Time Complexity (TC):
# - Initial border traversal (Step 5): You iterate over all border cells, which takes O(m + n) time.
#   Here, m is the number of rows, and n is the number of columns.
# - DFS traversal (Step 4): For each 'O' on the border, you perform a DFS to mark all connected 'O's.
#   In the worst case, DFS visits all cells, which takes O(m * n) time.
# - Final traversal (Step 6): After marking all border-connected 'O's, you traverse the entire board 
#   again to flip and revert cells, which takes O(m * n) time.
# - Overall Time Complexity: O(m * n) since the most time-consuming operation is visiting every cell during DFS and the final traversal.

# Space Complexity (SC):
# - DFS recursion stack: In the worst case, the recursion depth of DFS can reach O(m * n) if the board 
#   is filled with 'O's. DFS uses recursion, which consumes stack space proportional to the depth.
# - No additional data structures are used other than a few variables (e.g., 'm', 'n', and 'dirs').
# - Overall Space Complexity: O(m * n), primarily due to the recursion stack from DFS in the worst case.
