from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # m: number of rows, n: number of columns
        m, n = len(grid), len(grid[0])
        
        # res: keeps track of the number of steps taken (the BFS level)
        # q: deque (queue) for BFS, initialized with the start point (0,0) and k=0 (no obstacles removed)
        # vis: a set to track visited states (row, col, k), where k represents the number of obstacles removed
        res, q, vis = 0, deque([(0, 0, 0)]), {(0, 0, 0)}
        
        # Directions for movement: right (0,1), down (1,0), left (0,-1), up (-1,0)
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # Helper function to check if a cell is within the grid bounds
        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n

        # Helper function to check if we reached the bottom-right corner (destination)
        def is_boundary(r, c):
            return r == m - 1 and c == n - 1

        # BFS loop: continue until there are no more positions to explore
        while q:
            size = len(q)  # Current BFS level size (all nodes at this level)
            
            # Process all nodes in the current level
            for _ in range(size):
                # Get the current position (row, col) and the number of obstacles removed (curr_k)
                row, col, curr_k = q.popleft()
                
                # If we reached the bottom-right corner, return the number of steps taken (res)
                if is_boundary(row, col):
                    return res
                
                # Explore all four possible directions
                for dx, dy in dirs:
                    # Calculate the new position (next_row, next_col) and maintain the obstacle count
                    next_row, next_col, next_k = row + dx, col + dy, curr_k

                    # Check if the new position is within bounds
                    if is_valid(next_row, next_col):
                        # If the new position has an obstacle (grid value 1), increment the obstacle count
                        if grid[next_row][next_col] == 1:
                            next_k += 1
                        
                        # If the new position is valid (within the obstacle removal limit) and has not been visited
                        if next_k <= k and (next_row, next_col, next_k) not in vis:
                            # Mark the position as visited
                            vis.add((next_row, next_col, next_k))
                            # Add the new position to the queue for further exploration
                            q.append((next_row, next_col, next_k))
            
            # Increment the step count (res) after processing one BFS level
            res += 1

        # If we exhaust the queue without reaching the destination, return -1 (no valid path)
        return -1
