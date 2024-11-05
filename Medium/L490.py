# DFS
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

# Time Complexity (TC): O(m * n), where m is the number of rows and n is the number of columns.
# Each cell is visited at most once, as each cell is only added to the visited set one time.
#
# Space Complexity (SC): O(m * n), for the visited set and the recursion stack.
# The visited set may store up to m * n cells, and the recursion depth in the worst case
# can also go up to m * n, depending on the structure of the maze and paths explored.

# BFS
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])  # Dimensions of the maze
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # Directions: right, down, left, up

        # Helper function to check if a cell is within bounds and not a wall
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and maze[x][y] != 1

        # Helper function to check if the current cell is the destination
        def reached_dest(x, y):
            return [x, y] == destination

        # Initialize the BFS queue and visited set
        vis, q = set(), deque([(start[0], start[1])])
        
        # BFS loop
        while q:
            x, y = q.popleft()  # Dequeue the current cell
            key = (x, y)
            
            # Check if the destination is reached
            if reached_dest(x, y):
                return True
            
            # Skip cells that are invalid or already visited
            if not is_valid(x, y) or key in vis:
                continue

            vis.add(key)  # Mark the current cell as visited
            
            # Explore all four directions
            for dx, dy in dirs:
                r, c = x, y
                
                # Roll in the current direction until hitting a wall or boundary
                while is_valid(r + dx, c + dy):
                    r, c = r + dx, c + dy
                
                # After reaching the last valid cell in this direction, add it to the queue if unvisited
                if (r, c) not in vis:
                    q.append((r, c))
        
        # Return False if no path to the destination is found
        return False

# Time Complexity (TC): O(m * n), where m is the number of rows and n is the number of columns.
# Each cell is visited at most once in each direction due to the visited set, making the process efficient.

# Space Complexity (SC): O(m * n), for the queue and visited set.
# The queue can contain up to m * n cells in the worst case, and the visited set also stores up to m * n cells.
