class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # Define the possible directions in which the ball can roll: right, down, left, up
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        # `vis` keeps track of visited positions in the maze to prevent re-processing the same position
        vis = set()  # A set to store visited cells
        m, n = len(maze), len(maze[0])  # `m` is the number of rows, `n` is the number of columns in the maze

        # Helper function to check if a position (r, c) is within bounds and not a wall (value 1)
        def is_valid(r, c):
            # Return True if (r, c) is a valid position (inside maze and not a wall)
            return 0 <= r < m and 0 <= c < n and maze[r][c] != 1

        # Recursive function to explore the maze
        # It takes the current position (x, y) as input, starting from the initial start point
        def solve(x=start[0], y=start[1]):
            key = (x, y)  # Current position key (tuple) to mark as visited

            # If the current position has already been visited, return False (don't re-process it)
            if key in vis:
                return False

            # If the current position matches the destination, return True (found a path)
            if x == destination[0] and y == destination[1]:
                return True

            # Mark the current position as visited
            vis.add(key)

            # Try to move in all four possible directions
            for dx, dy in dirs:
                row, col = x, y  # Start from the current position
                
                # Keep moving in the current direction (dx, dy) until we hit a wall or the boundary of the maze
                while is_valid(row + dx, col + dy):
                    row, col = row + dx, col + dy  # Update to the next valid position

                # After reaching the farthest point in the current direction, recursively solve from there
                if solve(row, col):
                    return True  # If a valid path to the destination is found, return True
            
            # If no valid path is found from this position, return False
            return False

        # Start the recursive solving from the start position
        return solve()