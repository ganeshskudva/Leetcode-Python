class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize the grid
        dp = [[0] * n for _ in range(m)]  # O(m * n) space
        for x, y in guards + walls:  # O(g + w) time
            dp[x][y] = 1  # Mark guards and walls in the grid

        # Directions for traversal (right, down, left, up)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # Helper function to validate cells
        def is_valid(x, y):
            # Valid if within bounds and not a guard or wall
            return 0 <= x < m and 0 <= y < n and dp[x][y] != 1

        # Mark guarded cells
        for x, y in guards:  # O(g) for iterating guards
            for dx, dy in directions:  # O(4) for 4 directions
                curr_x, curr_y = x, y
                while is_valid(curr_x + dx, curr_y + dy):  # Up to O(m + n) per direction
                    curr_x += dx
                    curr_y += dy
                    dp[curr_x][curr_y] = 2  # Mark the cell as guarded

        # Count unguarded cells
        result = sum(1 for i in range(m) for j in range(n) if dp[i][j] == 0)  # O(m * n) time

        return result

# Time Complexity (TC):
# - Grid initialization: O(m * n)
# - Marking guards and walls: O(g + w)
# - Traversing for guard directions: O(g * (m + n)) (up to 4 directions per guard)
# - Counting unguarded cells: O(m * n)
# Total: O(g * (m + n) + m * n)

# Space Complexity (SC):
# - Grid storage: O(m * n)
# - Auxiliary variables and directions: O(1)
# Total: O(m * n)
