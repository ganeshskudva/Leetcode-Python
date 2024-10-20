import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Directions for moving in the grid: down, right, up, left
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        # Get the number of rows (m) and columns (n) of the grid
        m, n = len(heights), len(heights[0])
        
        # Priority queue to process cells in order of minimum effort (cost)
        # The priority queue stores tuples of (cost, row, col)
        pq = [(0, 0, 0)]  # Start from the top-left corner (0, 0) with an initial cost of 0
        
        # Dictionary to keep track of the minimum effort needed to reach each cell
        # Initialize the cost for every cell to infinity (unreachable at first)
        cost = { (row, col): float('inf') for col in range(n) for row in range(m) }
        cost[(0, 0)] = 0  # The starting point (0, 0) has a cost of 0

        # Helper function to check if a cell is within grid bounds
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n
        
        # Process the priority queue (Dijkstra's algorithm)
        while pq:
            # Pop the cell with the smallest current effort from the priority queue
            curr_cost, row, col = heapq.heappop(pq)
            
            # If we reached the bottom-right corner, return the minimum effort required
            if row == m - 1 and col == n - 1:
                return curr_cost
            
            # Get the current cell's height
            curr_height = heights[row][col]
            
            # Explore all 4 possible directions (down, right, up, left)
            for dx, dy in dirs:
                new_row, new_col = row + dx, col + dy  # Calculate new cell coordinates
                
                if is_valid(new_row, new_col):  # Check if the new cell is valid (within grid bounds)
                    # Get the neighboring cell's height
                    neigh_height = heights[new_row][new_col]
                    
                    # Calculate the effort to move to the neighboring cell
                    # The effort is the maximum of the current path's cost and the height difference between the two cells
                    new_cost = max(curr_cost, abs(neigh_height - curr_height))
                    
                    # If the new cost is less than the previously recorded cost for the neighboring cell,
                    # update it and push the cell to the priority queue
                    if new_cost < cost[(new_row, new_col)]:
                        cost[(new_row, new_col)] = new_cost  # Update the minimum cost to reach this cell
                        heapq.heappush(pq, (new_cost, new_row, new_col))  # Push the new cell into the priority queue with its updated cost
        
        # Return the minimum effort required to reach the bottom-right corner
        # In a valid case, this line is guaranteed to be reached when we pop the bottom-right corner from the queue
        return cost[(m - 1, n - 1)]

# Time Complexity (TC): O(m * n * log(m * n)), where m is the number of rows and n is the number of columns.
#   - We have to process each cell (m * n) once. Each insertion and removal from the priority queue takes O(log(m * n)) time.
#   - Thus, the overall time complexity is O(m * n * log(m * n)).

# Space Complexity (SC): O(m * n), where m is the number of rows and n is the number of columns.
#   - We need to store the cost of each cell in the cost dictionary and also maintain the priority queue (which 
