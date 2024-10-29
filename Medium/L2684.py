class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # Initialize dimensions of the grid and a dictionary for memoization
        m, n = len(grid), len(grid[0])
        mp = defaultdict(int)  # mp stores the max moves for each cell (x, y)
        
        # Define possible directions: right, down-right, and up-right
        dirs = [(0, 1), (1, 1), (-1, 1)]

        # Check if a cell is within grid boundaries
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        # Recursive function to calculate max moves from (x, y)
        def solve(x, y):
            key = (x, y)  # Use (x, y) as the key for memoization
            if key in mp:  # Return cached result if already computed
                return mp[key]
            
            res = 0  # Initialize result for max moves from this cell
            for dx, dy in dirs:
                next_x, next_y = x + dx, y + dy
                # Move to the next cell only if it's within bounds and has a higher value
                if is_valid(next_x, next_y) and grid[next_x][next_y] > grid[x][y]:
                    res = max(res, 1 + solve(next_x, next_y))  # Increment path length
            
            mp[key] = res  # Cache the result for (x, y)
            return mp[key]

        # Compute max moves for each cell in the first column
        return max(solve(i, 0) for i in range(m))

# Time Complexity (TC):
# - Each cell in the grid can be visited only once due to memoization.
# - For each cell, we explore up to 3 directions (constant work).
# - Therefore, the time complexity is O(m * n).

# Space Complexity (SC):
# - Memoization dictionary `mp` can store results for each cell, taking up O(m * n) space.
# - The recursive call stack can go as deep as O(m + n) in the worst case.
# - Overall space complexity is O(m * n) due to memoization storage.
