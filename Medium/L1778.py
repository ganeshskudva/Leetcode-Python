from collections import deque

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:

        # Initialize movement directions and their opposites for backtracking
        dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        anti = {"U": "D", "D": "U", "L": "R", "R": "L"}

        # Dictionary to track valid positions and whether they are the target
        isValid = {}
        isValid[(0, 0)] = master.isTarget()  # Start at (0, 0)

        # Depth-First Search (DFS) to explore all reachable positions
        def dfs(r, c):
            for d in dirs:
                dx, dy = dirs[d]
                nr, nc = r + dx, c + dy
                if (nr, nc) not in isValid and master.canMove(d):
                    # Move to the next cell
                    master.move(d)
                    # Mark if the position is valid and if it is the target
                    isValid[(nr, nc)] = master.isTarget()
                    # Recur for the next position
                    dfs(nr, nc)
                    # Move back to the previous position
                    master.move(anti[d])

        # Start DFS from the initial position (0, 0)
        dfs(0, 0)

        # Breadth-First Search (BFS) to find the shortest path to the target
        qu = deque([(0, 0, 0)])  # (row, column, steps)
        seen = set()
        
        while qu:
            r, c, step = qu.popleft()
            # If the target is found, return the distance (steps)
            if isValid[(r, c)]:
                return step

            # Explore all four possible directions
            for nr, nc in [[r + 1, c], [r - 1, c], [r, c - 1], [r, c + 1]]:
                if (nr, nc) in isValid and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    qu.append((nr, nc, step + 1))

        # Return -1 if the target is not reachable
        return -1

# Time Complexity (TC): O(V + E)
# - The DFS explores each reachable cell once, which is O(V), where V is the number of reachable cells.
# - BFS also explores each cell and edge, resulting in O(V + E), where E is the number of edges between reachable cells.

# Space Complexity (SC): O(V)
# - The isValid dictionary stores each reachable cell, which requires O(V) space.
# - The BFS queue and the seen set each store up to O(V) cells.
# - Overall, the space complexity is O(V).
