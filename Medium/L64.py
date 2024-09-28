class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])

        # Dictionary `mp` for memoization to store the minimum path sum for each cell
        mp = {}
        
        # Helper function to check if a given cell (x, y) is valid within grid bounds
        def is_valid(x, y):
            # Return True if the cell is within the grid boundaries, False otherwise
            return 0 <= x < rows and 0 <= y < cols

        # Recursive function to calculate the minimum path sum from cell (r, c) to the bottom-right corner
        def solve(r, c):
            # If the cell is out of bounds, return a large number (infinity) to avoid using this path
            if not is_valid(r, c):
                return float('inf')
            
            # If the current cell is the bottom-right corner, return its value (base case)
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            
            # Memoization: If the solution for this cell is already computed, return the cached result
            key = (r, c)
            if key in mp:
                return mp[key]

            # Compute the minimum path sum by moving either down or right
            # The result is stored in the memoization dictionary `mp` for future reference
            mp[key] = grid[r][c] + min(solve(r + 1, c), solve(r, c + 1))
            
            # Return the computed minimum path sum for the current cell
            return mp[key]

        # Start solving from the top-left corner of the grid (0, 0)
        return solve(0, 0)
