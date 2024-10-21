class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # Directions for moving right, down, left, up
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        # Get dimensions of the grid: m is the number of rows, n is the number of columns
        m, n = map(len, (grid, grid[0]))
        
        # Initialize distance matrix with infinity to keep track of the minimum obstacles at each cell
        dist = [[float('inf')] * n for _ in range(m)]
        
        # Deque to process nodes, starting at (0, 0) with 0 obstacles removed
        q = deque([(0, 0, 0)])

        # Helper function to check if a cell is within bounds and not yet visited
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and dist[x][y] == float('inf')

        # Perform BFS-like traversal
        while q:
            obstacle, row, col = q.popleft()  # Get the current node with the number of obstacles removed so far

            # Early exit: if we reached the bottom-right corner, return the result immediately
            if row == m - 1 and col == n - 1:
                return obstacle

            for dx, dy in dirs:  # Explore all four possible directions
                next_row, next_col = row + dx, col + dy  # Calculate the next cell coordinates
                if is_valid(next_row, next_col):  # Check if the cell is valid to visit
                    if grid[next_row][next_col] == 1:  # If the next cell is an obstacle (1)
                        dist[next_row][next_col] = obstacle + 1  # Update distance with one more obstacle removed
                        q.append((obstacle + 1, next_row, next_col))  # Add to the back of the queue (lower priority)
                    else:  # If the next cell is not an obstacle (0)
                        dist[next_row][next_col] = obstacle  # Keep the obstacle count the same
                        q.appendleft((obstacle, next_row, next_col))  # Add to the front of the queue (higher priority)

        # Return the minimum number of obstacles to remove to reach the bottom-right corner
        return dist[-1][-1]

# Time Complexity (TC):
# Each cell is processed at most once. There are m * n cells in the grid.
# Each cell is dequeued and we check its four neighbors, leading to a time complexity of O(m * n).

# Space Complexity (SC):
# The space is used for the distance matrix `dist`, which is O(m * n),
# and for the deque `q`, which can also store O(m * n) elements in the worst case.
# Therefore, the overall space complexity is O(m * n).
