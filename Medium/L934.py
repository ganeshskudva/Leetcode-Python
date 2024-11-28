from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()

        # Helper function to check if a cell is valid
        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n and not visited[i][j] and A[i][j] == 1

        # Closure for DFS to mark the first island and collect its boundary
        def dfs(i, j):
            if not is_valid(i, j):  # Use the helper function
                return
            visited[i][j] = True
            queue.append((i, j))  # Add the boundary cells of the first island
            for di, dj in directions:
                dfs(i + di, j + dj)

        # Step 1: Find the first island using DFS
        found = False
        for i in range(m):
            if found:
                break
            for j in range(n):
                if A[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        # Step 2: Perform BFS to expand the island and find the shortest path
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        if A[nx][ny] == 1:
                            return steps  # Found the second island
                        queue.append((nx, ny))
                        visited[nx][ny] = True
            steps += 1

        return -1  # Should not reach here if the input is valid

# Time Complexity (TC): O(m * n)
# Explanation:
# - The DFS explores all cells in the first island, which takes O(m * n) in the worst case.
# - The BFS explores the remaining cells, which also takes O(m * n).
# - Overall complexity is O(m * n).

# Space Complexity (SC): O(m * n)
# Explanation:
# - The `visited` matrix uses O(m * n) space.
# - The `queue` can grow to O(m * n) in the worst case.
# - Overall space complexity is O(m * n).
