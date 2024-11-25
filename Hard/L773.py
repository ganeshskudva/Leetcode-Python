from collections import deque
from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        Solve the sliding puzzle problem using BFS.

        Args:
        board (List[List[int]]): A 2D list representing the initial board configuration.

        Returns:
        int: Minimum number of moves to solve the puzzle, or -1 if unsolvable.
        """
        # Target configuration for the puzzle
        target = "123450"
        # Possible moves for each index in the flattened board
        moves = {
            0: [1, 3], 
            1: [0, 2, 4], 
            2: [1, 5], 
            3: [0, 4], 
            4: [1, 3, 5], 
            5: [2, 4]
        }
        
        # Convert the board into a single string
        start = ''.join(str(num) for row in board for num in row)
        
        # BFS setup
        visited = set()  # To keep track of visited configurations
        visited.add(start)
        queue = deque([(start, 0)])  # Queue stores tuples (current board, steps)
        
        while queue:
            curr, steps = queue.popleft()
            if curr == target:
                return steps  # Found the solution
            
            zero_idx = curr.index('0')  # Find the index of '0' (empty space)
            
            # Explore all possible moves for '0'
            for move in moves[zero_idx]:
                # Swap '0' with the adjacent number
                next_board = list(curr)
                next_board[zero_idx], next_board[move] = next_board[move], next_board[zero_idx]
                next_board_str = ''.join(next_board)
                
                # If not visited, add the new configuration to the queue
                if next_board_str not in visited:
                    visited.add(next_board_str)
                    queue.append((next_board_str, steps + 1))
        
        return -1  # If no solution is found


# Time Complexity: O(n!), where n is the number of elements in the board (6 in this case),
# as we are exploring all possible permutations of the board configuration.

# Space Complexity: O(n!), to store all visited board configurations in the queue and visited set.