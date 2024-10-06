class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Step 1: Get the dimensions of the grid.
        # 'm' is the number of rows, 'n' is the number of columns.
        m, n = len(grid), len(grid[0])

        # 'vis' is a set to keep track of visited cells, and 'tot' will store the maximum island area found.
        vis, tot = set(), 0

        # Step 2: Define the four possible directions (right, down, left, up) to explore the neighboring cells.
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # Step 3: Helper function to check if a cell (x, y) is valid for exploration.
        # A valid cell is within grid bounds and is part of an island (grid[x][y] == 1).
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 1

        # Step 4: DFS function to explore the connected island cells.
        # It starts from cell (x, y) and explores all its connected cells to calculate the island's area.
        def solve(x, y):
            # If the current cell is out of bounds or is water (grid[x][y] != 1), return 0.
            if not is_valid(x, y):
                return 0
            # If the current cell has already been visited, return 0.
            if (x, y) in vis:
                return 0

            # Mark the current cell as visited.
            vis.add((x, y))

            # Initialize the area count for the current island.
            cnt = 0
            # Step 5: Explore all four neighboring cells (right, down, left, up).
            for d in dirs:
                cnt += solve(x + d[0], y + d[1])

            # Return the area of this part of the island (including the current cell).
            return cnt + 1

        # Step 6: Iterate through each cell in the grid.
        for i in range(m):
            for j in range(n):
                # If the current cell is a valid land cell ('1') and hasn't been visited yet,
                # start a DFS from that cell to calculate the area of the island.
                if is_valid(i, j) and (i, j) not in vis:
                    # Update the maximum island area found so far.
                    tot = max(tot, solve(i, j))

        # Step 7: Return the largest area of the island found.
        return tot

# Time Complexity (TC):
# - Each cell is visited at most once during the DFS. For each land cell, the DFS explores its four neighboring cells.
# - The total number of cells in the grid is m * n, where m is the number of rows and n is the number of columns.
# - Therefore, the overall time complexity is O(m * n), as each cell is processed once.

# Space Complexity (SC):
# - The 'vis' set stores the coordinates of all visited land cells. In the worst case, all cells could be land, so 'vis' would store O(m * n) entries.
# - The DFS recursion stack can go as deep as O(m * n) in the worst case (if the entire grid is one big island).
# - Hence, the overall space complexity is O(m * n) due to the 'vis' set and recursion stack.

