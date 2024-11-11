# DFS
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # Get the dimensions of the board
        m, n = len(board), len(board[0])
        
        # Click position
        row, col = click[0], click[1]
        
        # Directions for the 8 possible adjacent cells
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        # Helper function to check if a cell is within board boundaries
        # Time Complexity: O(1) for each call
        # Space Complexity: O(1)
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        # Helper function to count adjacent mines for a cell
        # Time Complexity: O(1) because it checks a maximum of 8 neighboring cells
        # Space Complexity: O(1)
        def adj_mine(x, y):
            cnt = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    # Increment count if a mine ('M') is found in the neighborhood
                    if is_valid(i, j) and board[i][j] == 'M':
                        cnt += 1
            return cnt

        # Recursive function to reveal cells
        # Time Complexity: O(m * n) in the worst case, where m is the number of rows and n is the number of columns
        #   This happens if we need to reveal all cells due to no mines being adjacent to each cell.
        # Space Complexity: O(m * n) due to recursion depth in the worst case (if all cells are revealed).
        def solve(x, y):
            # Base cases to stop recursion
            if not is_valid(x, y):
                return
            if board[x][y] != 'E':  # If already revealed or marked
                return
            
            # Count adjacent mines around the current cell
            mine = adj_mine(x, y)
            if mine > 0:
                # If there are adjacent mines, mark cell with the mine count
                board[x][y] = f'{mine}'
            else:
                # If no adjacent mines, mark cell as 'B' and reveal neighbors
                board[x][y] = 'B'
                for dx, dy in dirs:
                    solve(x + dx, y + dy)

        # Main function logic
        if board[row][col] == 'M':
            # If the clicked cell is a mine, change it to 'X' to indicate explosion
            board[row][col] = 'X'
        else:
            # If the clicked cell is empty ('E'), start revealing cells recursively
            solve(row, col)

        return board

# Time Complexity (TC):
# - Each cell in the board is processed at most once. The main complexity comes from the `solve` function,
#   which may visit all cells in the board in the worst case, making the time complexity O(m * n), 
#   where m is the number of rows and n is the number of columns.
# - Checking adjacent cells for mines in `adj_mine` is constant time, O(1), as it only checks up to 8 neighbors.

# Space Complexity (SC):
# - The recursion depth for `solve` can reach up to O(m * n) in the worst case if all cells are revealed.
# - The directions list (`dirs`) and helper functions use O(1) space.
# - Overall space complexity: O(m * n).

# BFS
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        queue = deque([click])

        # Helper function to check if a cell is within bounds
        def is_valid(r: int, c: int) -> bool:
            return 0 <= r < m and 0 <= c < n

        while queue:
            row, col = queue.popleft()
            
            # Case 1: Clicked on a mine
            if board[row][col] == 'M':
                board[row][col] = 'X'
            
            # Case 2: Clicked on an empty cell ('E')
            else:
                # Step 1: Count adjacent mines
                count = 0
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if is_valid(r, c) and (board[r][c] == 'M' or board[r][c] == 'X'):
                        count += 1
                
                # Step 2: Update cell based on adjacent mine count
                if count > 0:
                    board[row][col] = str(count)
                else:
                    board[row][col] = 'B'
                    # Step 3: Add adjacent cells to queue if they are 'E'
                    for dr, dc in directions:
                        r, c = row + dr, col + dc
                        if is_valid(r, c) and board[r][c] == 'E':
                            queue.append((r, c))
                            board[r][c] = 'B'  # Mark as visited to prevent re-adding

        return board

# Time Complexity (TC):
# - Each cell is visited at most once. For each cell, we check up to 8 neighbors, so the time complexity is O(m * n),
#   where m is the number of rows and n is the number of columns.

# Space Complexity (SC):
# - The space complexity is O(m * n) for the queue in the worst case, as all cells could be added to the queue.
# - The `directions` list and `is_valid` function use O(1) space.
# - Overall space complexity: O(m * n).
