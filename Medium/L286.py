class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Modifies the grid 'rooms' in-place to fill each empty room with the distance to the nearest gate.
        """
        # Step 1: Base case to handle an empty grid or no columns in the grid.
        if not rooms or not len(rooms[0]):
            return
        
        # Step 2: Define variables.
        # 'inf' is the placeholder value for empty rooms (2147483647).
        inf = 2147483647
        
        # Define possible directions for movement: right, down, left, up.
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        # 'q' is a queue to perform BFS (Breadth-First Search).
        # 'm' is the number of rows, and 'n' is the number of columns in the grid.
        q, m, n = deque(), len(rooms), len(rooms[0])

        # Step 3: Find all the gates (rooms with value 0) and add them to the queue.
        # These will act as starting points for the BFS.
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:  # If it's a gate (rooms[i][j] == 0)
                    q.append((i, j))  # Add the gate coordinates to the queue.

        # Step 4: Helper function to check if a cell (x, y) is within bounds and is an empty room (rooms[x][y] == inf).
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and rooms[x][y] == inf

        # Step 5: BFS from all gates simultaneously.
        # For each cell popped from the queue, we check its four neighboring cells (right, down, left, up).
        while q:
            row, col = q.popleft()  # Get the current cell coordinates.
            dist = rooms[row][col] + 1  # Distance to the neighboring cell is the current cell's distance + 1.
            
            # Explore all four directions.
            for d in dirs:
                new_x, new_y = row + d[0], col + d[1]  # New coordinates after moving in direction 'd'.
                
                # If the new cell is valid (an empty room), update its distance and add it to the queue.
                if is_valid(new_x, new_y):
                    rooms[new_x][new_y] = dist  # Update the empty room's distance to the nearest gate.
                    q.append((new_x, new_y))  # Add the new cell to the queue for further exploration.

# Time Complexity (TC):
# - Initial iteration to identify all gates takes O(m * n), where m is the number of rows and n is the number of columns.
# - BFS processes each cell at most once. For each cell, we explore its four neighbors, which takes O(1) time.
# - The total number of cells is m * n, so BFS takes O(m * n).
# - Overall, the time complexity is O(m * n) because we iterate through all cells both in the initial setup and during BFS.

# Space Complexity (SC):
# - The queue 'q' can hold up to O(m * n) elements in the worst case, where every cell is processed.
# - The 'dirs' list uses constant space O(1).
# - The input 'rooms' is modified in place, so no extra space is used for storing the output.
# - Overall, the space complexity is O(m * n) due to the queue, which can store up to m * n cells.
