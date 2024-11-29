def minimumTime(self, grid: List[List[int]]) -> int:
    # If both adjacent cells of the starting position are blocked (> 1), return -1 as traversal is impossible.
    if grid[0][1] > 1 and grid[1][0] > 1: 
        return -1

    m, n = len(grid), len(grid[0])  # Dimensions of the grid
    visited = set()  # To track visited cells and avoid redundant processing
    pq = [(grid[0][0], 0, 0)]  # Priority queue initialized with (time, row, col)
    
    while pq:
        time, row, col = heappop(pq)  # Get the cell with the smallest time
        # If we've reached the bottom-right corner, return the time
        if row == m - 1 and col == n - 1: 
            return time
        # Skip already visited cells
        if (row, col) in visited: 
            continue
        visited.add((row, col))  # Mark the current cell as visited
        
        # Explore all valid neighbors (up, down, left, right)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            r, c = row + dr, col + dc
            # Check if the neighbor is within bounds and not visited
            if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                # Calculate wait time to align with the cell's availability
                wait = 1 if ((grid[r][c] - time) % 2 == 0) else 0
                # Push the neighbor with the updated time into the priority queue
                heappush(pq, (max(time + 1, grid[r][c] + wait), r, c))
    
    # If the destination cannot be reached, return -1
    return -1

# Time Complexity: O(m * n * log(m * n))
# - Each cell is processed at most once, and the priority queue operations (heappush, heappop) take O(log(m * n)).
# - Total complexity is proportional to the number of cells and logarithmic in the size of the grid.

# Space Complexity: O(m * n)
# - The priority queue and the visited set each take up to O(m * n) space in the worst case.
