## Optimized

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # Step 1: Get the dimensions of the board.
        m, n = len(board), len(board[0])
        cnt = 0

        # Step 2: Iterate through each cell in the board.
        for i in range(m):
            for j in range(n):
                # Step 3: Check if the current cell is part of a new battleship.
                # - The current cell should be 'X' (a part of a battleship).
                # - The cell directly above it should not be 'X' (no continuation from the top).
                # - The cell directly to the left of it should not be 'X' (no continuation from the left).
                if board[i][j] == 'X':
                    if i > 0 and board[i-1][j] == 'X':
                        continue  # Skip if there is an 'X' above (it's not a new ship).
                    if j > 0 and board[i][j-1] == 'X':
                        continue  # Skip if there is an 'X' to the left (it's not a new ship).
                    # Increment the count if it's the start of a new battleship.
                    cnt += 1

        # Step 4: Return the total number of battleships found on the board.
        return cnt

# Time Complexity (TC):
# - We iterate through each cell in the grid exactly once, performing constant-time operations at each step.
# - Since there are m rows and n columns, the overall time complexity is O(m * n),
#   where m is the number of rows and n is the number of columns in the grid.

# Space Complexity (SC):
# - We do not use any additional data structures like a visited set or recursion stack.
# - The space used is constant, as we only use a few variables (m, n, cnt) and no additional space is required.
# - Therefore, the overall space complexity is O(1), which is optimal.


## DFS

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # Step 1: Get the dimensions of the board.
        # 'm' is the number of rows, 'n' is the number of columns.
        m, n = len(board), len(board[0])

        # Define the possible directions (right, down, left, up) to explore neighboring cells during DFS.
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # 'vis' is a set to keep track of visited cells.
        # 'cnt' will store the number of distinct battleships.
        vis, cnt = set(), 0

        # Step 2: Helper function to check if a cell (x, y) is valid for exploration.
        # A valid cell is within the grid bounds and contains an 'X' (part of a battleship).
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and board[x][y] == 'X'

        # Step 3: Depth-first search (DFS) function to explore all connected 'X' cells (battleship cells).
        # It recursively visits all unvisited 'X' cells connected to the starting cell (x, y).
        def solve(x, y):
            # If the current cell is out of bounds or is not part of a battleship, return.
            if not is_valid(x, y):
                return
            # If the current cell has already been visited, return.
            key = (x, y)
            if key in vis:
                return

            # Mark the current cell as visited.
            vis.add(key)

            # Explore all four neighboring cells (right, down, left, up).
            for dx, dy in dirs:
                solve(x + dx, y + dy)

        # Step 4: Iterate through each cell in the board.
        for i in range(m):
            for j in range(n):
                # If the current cell is part of a battleship ('X') and hasn't been visited yet,
                # start a DFS from that cell to explore the entire battleship.
                if is_valid(i, j) and (i, j) not in vis:
                    solve(i, j)  # Perform DFS from cell (i, j).
                    cnt += 1     # Increment the battleship count after exploring the entire ship.

        # Step 5: Return the total number of battleships found on the board.
        return cnt

# Time Complexity (TC):
# - Each cell in the board is processed once, either directly during the iteration or through DFS exploration.
# - The overall time complexity is O(m * n), where m is the number of rows and n is the number of columns, 
#   as each cell is visited at most once.

# Space Complexity (SC):
# - The 'vis' set stores the coordinates of all visited cells. In the worst case, all cells could be part of battleships, 
#   so the 'vis' set would store O(m * n) entries.
# - The DFS recursion stack can go as deep as O(m * n) in the worst case, especially if the battleship occupies a large area.
# - Therefore, the overall space complexity is O(m * n) due to the 'vis' set and the DFS recursion stack.
