# Using Heaps

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # Initialize the min-heap (priority queue) with the start position and initial distance 0
        # Each element in the heap will be a tuple: (distance, x, y)
        heap = [(0, start[0], start[1])]
        
        # Directions for movement: right (0,1), down (1,0), left (0,-1), up (-1,0)
        # These represent the change in (x, y) coordinates for each direction
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        # m = number of rows in the maze, n = number of columns in the maze
        m, n = len(maze), len(maze[0])
        
        # Initialize a 2D list `distance` where each cell holds the shortest distance to that point
        # Initially, set all distances to infinity (since we haven't visited any cell yet)
        distance = [[float('inf')] * n for _ in range(m)]
        
        # The starting point has a distance of 0 from itself
        distance[start[0]][start[1]] = 0
        
        # Helper function to check if the position (x, y) is valid:
        # It must be within the bounds of the maze and not be a wall (maze[x][y] == 1 is a wall)
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and maze[x][y] != 1
        
        # Helper function to check if the current position (x, y) is the destination
        def reached_dest(x, y):
            return x == destination[0] and y == destination[1]
        
        # Main loop: Dijkstra-like algorithm using a priority queue (min-heap)
        # The heap will always give us the node with the smallest distance first
        while heap:
            # Pop the cell with the smallest known distance from the heap
            dist, x, y = heapq.heappop(heap)
            
            # If this distance is greater than the best known distance to (x, y), skip it
            # This happens if we already processed a shorter path to this cell
            if dist > distance[x][y]:
                continue
            
            # If we reached the destination, return the distance immediately
            # Because we're using a priority queue, this is guaranteed to be the shortest path
            if reached_dest(x, y):
                return dist
            
            # Explore all four possible directions from the current cell
            for dx, dy in dirs:
                # Start from the current cell (x, y) and move in the direction (dx, dy)
                r, c, new_dist = x, y, dist  # r and c are row and column indices, new_dist is the distance
                
                # Roll the ball until it hits a wall or goes out of bounds
                # While the next cell in the direction is valid (i.e., within bounds and not a wall)
                while is_valid(r + dx, c + dy):
                    r += dx  # Move in the x-direction
                    c += dy  # Move in the y-direction
                    new_dist += 1  # Increase the distance by 1 for each move
                
                # If we've found a shorter path to (r, c), update the distance and push it to the heap
                if new_dist < distance[r][c]:
                    distance[r][c] = new_dist  # Update the shortest distance to this cell
                    heapq.heappush(heap, (new_dist, r, c))  # Push the new distance and position to the heap
        
        # If we exit the loop without having reached the destination, return -1
        # This means there is no valid path to the destination
        return -1 if distance[destination[0]][destination[1]] == float('inf') else distance[destination[0]][destination[1]]


# Normal BFS using deque

from collections import deque

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # Initialize result to infinity (as we are looking for the minimum distance)
        # m = number of rows, n = number of columns in the maze
        # Initialize the deque with the start point (x, y, distance traveled so far)
        res, m, n, q = float('inf'), len(maze), len(maze[0]), deque([(start[0], start[1], 0)])
        
        # Directions for movement: right, down, left, up
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        # Initialize a distance matrix where each cell stores the minimum distance to reach that point
        # Initially set all distances to infinity since we haven't processed any points yet
        length = [[float('inf') for _ in range(n)] for _ in range(m)]
        
        # Helper function to check if a cell (x, y) is valid: within bounds and not a wall
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and maze[x][y] != 1
        
        # Helper function to check if the current cell (x, y) is the destination
        def reached_dest(x, y):
            return x == destination[0] and y == destination[1]
        
        # BFS loop: process all positions in the queue
        while q:
            # Pop the current position and distance from the front of the queue
            x, y, dist = q.popleft()

            # If we've already found a shorter path to (x, y), skip further processing for this cell
            if length[x][y] <= dist:
                continue
            
            # Otherwise, update the shortest distance to reach this cell
            length[x][y] = dist
            
            # If we've reached the destination, update the result with the minimum distance
            if reached_dest(x, y):
                res = min(dist, res)
            
            # Explore all four possible directions from the current cell
            for dx, dy in dirs:
                r, c, d = x, y, dist  # Initialize new coordinates (r, c) and distance (d)
                
                # Keep moving in the current direction until hitting a wall or going out of bounds
                while is_valid(r + dx, c + dy):
                    r += dx  # Move in the direction dx
                    c += dy  # Move in the direction dy
                    d += 1   # Increase the distance traveled
                
                # Add the new position and its distance to the queue for further processing
                q.append((r, c, d))
        
        # If we were unable to reach the destination, return -1, otherwise return the minimum distance found
        return -1 if res == float('inf') else res
