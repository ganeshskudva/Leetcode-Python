class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Step 1: Get the dimensions of the grid.
        # 'm' is the number of rows, 'n' is the number of columns.
        m, n, cnt = len(grid), len(grid[0]), 0
        
        # Step 2: Define a list of directions representing the four adjacent cells:
        # right (0, 1), down (1, 0), left (0, -1), and up (-1, 0).
        # These are used to explore the neighboring cells.
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        # Step 3: Helper function to check if a cell is water or out of bounds.
        def is_water(x, y):
            # A cell is considered water if it's out of grid bounds or has a value of 0 (water).
            return x < 0 or x == m or y < 0 or y == n or grid[x][y] == 0
        
        # Step 4: Helper function to check if a cell is land.
        def is_land(x, y):
            # A cell is land if it's within bounds and has a value of 1 (land).
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 1
        
        # Step 5: Traverse each cell in the grid using two nested loops.
        # Outer loop over rows: O(m)
        # Inner loop over columns: O(n)
        for i in range(m):
            for j in range(n):
                # If the current cell is land, we proceed to check its perimeter.
                if is_land(i, j):
                    # Step 6: For each land cell, check its four neighboring cells (right, down, left, up).
                    # Checking each of the four directions is a constant time operation: O(1)
                    for dx, dy in dirs:
                        # If the neighboring cell is water (or out of bounds), it's a boundary edge, 
                        # so we increase the perimeter count by 1.
                        if is_water(i + dx, j + dy):
                            cnt += 1
        
        # Step 7: After traversing the entire grid, return the total perimeter.
        # Time complexity is O(m * n) as each cell is processed once and 4 neighbors are checked in constant time.
        return cnt

# Time Complexity (TC): O(m * n)
# - We iterate over each cell in the grid (m rows, n columns) -> O(m * n).
# - For each land cell, we check 4 neighbors, which takes constant time -> O(1).
# - Thus, the overall time complexity is O(m * n).

# Space Complexity (SC): O(1)
# - We only use a few extra variables (e.g., 'cnt', 'dirs', and helper functions) which consume constant space.
# - No additional data structures that scale with input size are used.
# - Thus, the overall space complexity is O(1).
