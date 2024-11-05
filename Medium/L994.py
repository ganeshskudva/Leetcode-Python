from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh_cnt = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Helper function to check if a cell is valid for rotting
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 1

        # Count fresh oranges and add initial rotten oranges to the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_cnt += 1

        # If there are no fresh oranges, return 0 as no rotting is needed
        if fresh_cnt == 0:
            return 0

        # If there are no rotten oranges to start with, return -1
        if not q:
            return -1

        # Perform BFS to rot all reachable fresh oranges
        minutes = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    new_x, new_y = x + dx, y + dy
                    if is_valid(new_x, new_y):
                        grid[new_x][new_y] = 2  # Mark as rotten
                        q.append((new_x, new_y))
                        fresh_cnt -= 1

            # Increment minutes only if there are fresh oranges that just got rotten
            if q:
                minutes += 1

        # If there are still fresh oranges, return -1
        return -1 if fresh_cnt > 0 else minutes

# Time Complexity (TC): O(m * n)
#   - Each cell in the grid is visited at most once, as the BFS will process each cell once when rotting.
#   - Counting fresh and rotten oranges initially also takes O(m * n) time.
#   - Thus, the overall time complexity is O(m * n).

# Space Complexity (SC): O(m * n)
#   - The queue used for BFS can hold up to O(m * n) cells in the worst case.
#   - Additional space is used for the directions array and auxiliary variables, but these are negligible.
#   - Overall, the space complexity is O(m * n) due to the queue.
