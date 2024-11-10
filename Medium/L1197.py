from collections import deque
from typing import Tuple, Set

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # Define possible knight moves as a closure
        directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        # Use absolute values to reduce the search space, as moves are symmetric
        x, y = abs(x), abs(y)
        
        # Queue for BFS, starting from the origin (0, 0)
        queue = deque([(0, 0)])
        
        # Set to track visited positions
        visited: Set[Tuple[int, int]] = {(0, 0)}
        
        # BFS level (distance) initialization
        result = 0

        while queue:
            # Process all nodes at the current level
            for _ in range(len(queue)):
                curX, curY = queue.popleft()
                
                # Check if the target has been reached
                if (curX, curY) == (x, y):
                    return result
                
                # Try all knight moves from the current position
                for dx, dy in directions:
                    newX, newY = curX + dx, curY + dy
                    # Ensure the new position has not been visited and is within a reasonable bound
                    if (newX, newY) not in visited and newX >= -1 and newY >= -1:
                        queue.append((newX, newY))
                        visited.add((newX, newY))
            
            # Increment the number of moves after each level
            result += 1
        
        # If the target position is unreachable, return -1 (should not happen in this problem)
        return -1

# Time Complexity (TC):
# - BFS explores nodes in concentric circles around the origin until it reaches the target, requiring O(N^2) steps
#   in the worst case, where N is the maximum of |x| and |y|.
# - Symmetry optimization reduces the effective search space, but in the worst case, we still check up to O(N^2) nodes.
# - Overall time complexity: O(N^2).

# Space Complexity (SC):
# - The `visited` set stores each visited position, which can contain up to O(N^2) unique positions.
# - The `queue` for BFS can also hold up to O(N^2) nodes in the worst case.
# - Overall space complexity: O(N^2).
