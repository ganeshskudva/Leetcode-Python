class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # Define the four possible movement directions (right, down, left, up)
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        # Initialize a set 'vis' to track visited positions, and get dimensions of the maze (m rows, n columns)
        vis, m, n = set(), len(maze), len(maze[0])

        # Helper function to check if a given position (r, c) is valid (in bounds and not a wall)
        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n and maze[r][c] != 1

        # Recursive DFS function that attempts to find a path from (x, y)
        def solve(x=start[0], y=start[1]):
            # Create a key (tuple) for the current position (x, y)
            key = (x, y)

            # If this position has already been visited, return False (avoid cycles)
            if key in vis:
                return False

            # If the current position matches the destination, return True (path found)
            if x == destination[0] and y == destination[1]:
                return True

            # Mark the current position as visited
            vis.add(key)

            # Try moving in all four possible directions (defined in 'dirs')
            for dx, dy in dirs:
                # Initialize row and col to current position (x, y)
                row, col = x, y

                # Continue moving in the direction (dx, dy) until hitting a wall or going out of bounds
                while is_valid(row + dx, col + dy):
                    row, col = row + dx, col + dy

                # Recursively try to solve from the new stopped position
                if solve(row, col):
                    return True

        # Start the DFS search from the start position
        return solve()
