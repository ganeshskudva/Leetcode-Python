class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        """
        Find the shortest path to connect two islands in a binary matrix.
        
        Args:
            A: List[List[int]] - A binary grid where 1 represents land and 0 represents water.
        
        Returns:
            int - The shortest number of steps to connect the two islands.
        """
        m, n = len(A), len(A[0])  # Dimensions of the grid
        visited = [[False] * n for _ in range(m)]  # Visited array to track explored cells
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Possible moves: up, down, left, right
        queue = deque()  # Queue for BFS to expand the first island
        
        # Helper function to check if a cell is valid for DFS or BFS
        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n and not visited[i][j] and A[i][j] == 1
        
        # DFS to mark all cells of the first island and collect its boundary
        def dfs(i, j):
            if not is_valid(i, j):  # Check boundaries and if the cell is part of the island
                return
            visited[i][j] = True  # Mark cell as visited
            queue.append((i, j))  # Add the cell to the queue for BFS later
            # Explore all four possible directions
            for di, dj in directions:
                dfs(i + di, j + dj)
        
        # Step 1: Find the first island and mark its cells
        found = False  # Flag to stop after finding the first island
        for i in range(m):
            if found:  # Break outer loop once the first island is found
                break
            for j in range(n):
                if A[i][j] == 1:  # Start DFS from the first land cell encountered
                    dfs(i, j)
                    found = True
                    break  # Break inner loop
        
        # Step 2: Perform BFS to find the shortest path to the second island
        steps = 0  # Steps represent the distance from the first island
        while queue:
            size = len(queue)  # Number of cells to process at the current BFS level
            for _ in range(size):
                x, y = queue.popleft()  # Get the next cell to expand
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy  # Calculate the new coordinates
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:  # Check boundaries
                        if A[nx][ny] == 1:  # If a land cell from the second island is found
                            return steps  # Return the distance immediately
                        queue.append((nx, ny))  # Add the water cell to the queue to expand
                        visited[nx][ny] = True  # Mark the cell as visited
            steps += 1  # Increment steps after processing all cells at the current level
        
        return -1  # This point should never be reached for valid input

"""
Time Complexity (TC):
- Step 1 (DFS): In the worst case, we traverse all cells in the grid, O(m * n).
- Step 2 (BFS): In the worst case, we also traverse all cells, O(m * n).
- Overall TC: O(m * n).

Space Complexity (SC):
- Visited Array: O(m * n) to store the visited state of all cells.
- Queue for BFS: O(m * n) in the worst case if all cells are processed.
- Overall SC: O(m * n).
"""
