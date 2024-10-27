from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Check if starting or ending cell is blocked
        if grid[0][0] or grid[n-1][n-1]:
            return -1  # Return -1 if there's no valid path from start to end
        
        # Possible 8 directions to move (right, left, down, up, and all diagonals)
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [1, -1], [-1, 1]]
        
        # Set to keep track of visited cells
        seen = set()
        
        # Initialize queue for BFS with starting cell and distance 1
        queue = deque([(0, 0, 1)])  # Format: (row, column, distance)
        seen.add((0, 0))  # Mark the starting cell as visited

        def is_valid(x, y):
            # Check if the cell (x, y) is within bounds and is an open cell (0)
            return 0 <= x < n and 0 <= y < n and not grid[x][y]

        # BFS loop to explore the shortest path in all directions
        while queue:
            i, j, dist = queue.popleft()
            # Check if the destination is reached
            if i == n - 1 and j == n - 1:
                return dist  # Return the distance to the bottom-right corner
            
            # Explore all 8 directions
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                # Check if the move is valid and if the cell has not been visited
                if is_valid(x, y) and (x, y) not in seen:
                    seen.add((x, y))  # Mark cell as visited
                    queue.append((x, y, dist + 1))  # Enqueue with incremented distance

        # If destination is unreachable, return -1
        return -1

# Time Complexity (TC): O(n^2), where n is the grid dimension.
# - In the worst case, all cells are visited once in an n x n grid, making the time complexity O(n^2).

# Space Complexity (SC): O(n^2).
# - The queue may hold up to O(n^2) elements in the worst case, and the `seen` set also stores each visited cell,
#   both leading to a space complexity of O(n^2).
