class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Step 1: Define the four possible directions (right, down, left, up) 
        # to explore the neighboring cells during the DFS.
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # Step 2: Initialize the grid dimensions m (number of rows) and n (number of columns).
        # 'vis' is a set to keep track of visited cells, and 'cnt' is the number of islands.
        m, n, vis, cnt = len(grid), len(grid[0]), set(), 0

        # Step 3: Helper function to check if a cell (x, y) is valid for exploration.
        # A valid cell is within grid bounds and contains a '1' (land).
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == '1'

        # Step 4: Depth-first search (DFS) to explore all connected land cells (i.e., an island).
        # It recursively visits all unvisited land cells connected to the starting cell (x, y).
        def solve(x, y):
            # If the current cell is invalid or already visited, return.
            if not is_valid(x, y):
                return
            key = (x, y)
            if key in vis:
                return

            # Mark the current cell as visited.
            vis.add(key)

            # Explore all four neighboring cells (right, down, left, up).
            for dx, dy in dirs:
                solve(x + dx, y + dy)

        # Step 5: Iterate through each cell in the grid.
        for i in range(m):
            for j in range(n):
                # If the current cell is a valid land cell ('1') and hasn't been visited yet,
                # start a DFS from that cell to explore the entire island.
                if is_valid(i, j) and (i, j) not in vis:
                    solve(i, j)  # Perform DFS from cell (i, j).
                    cnt += 1     # Increment the island count after exploring the entire island.

        # Step 6: Return the total number of islands found in the grid.
        return cnt

# Time Complexity (TC):
# - We perform a DFS starting from each unvisited land cell.
# - Each cell is visited at most once during the DFS. For each cell, we check its four neighbors (constant work).
# - The total number of cells in the grid is m * n, where m is the number of rows and n is the number of columns.
# - Therefore, the overall time complexity is O(m * n), as each cell is processed once.

# Space Complexity (SC):
# - The 'vis' set stores the coordinates of all visited land cells. In the worst case, all cells could be land, so 'vis' would store O(m * n) entries.
# - The DFS recursion stack can also go as deep as O(m * n) in the worst case (if the entire grid is one big island).
# - Hence, the overall space complexity is O(m * n) due to the 'vis' set and recursion stack.
