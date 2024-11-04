from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        # Directions for moving up, down, left, and right
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(board), len(board[0])  # Board dimensions
        vis = set()  # Set to track visited cells

        # Check if cell (x, y) is within bounds and matches the target character
        def is_valid(x, y, ch):
            return 0 <= x < m and 0 <= y < n and board[x][y] == ch

        # Recursive DFS function to search for the word
        def solve(i, j, index):
            # Base case: if index reaches word length, word is found
            if index == len(word):
                return True
            # Check if cell is valid and not yet visited
            if not is_valid(i, j, word[index]) or (i, j) in vis:
                return False

            # Mark the current cell as visited
            vis.add((i, j))
            # Recursively search in all four directions
            found = any(solve(i + dx, j + dy, index + 1) for dx, dy in dirs)
            # Unmark the cell after exploring all options (backtracking)
            vis.remove((i, j))

            return found

        # Traverse each cell in the board to find the starting point for the word
        for i in range(m):
            for j in range(n):
                # If the cell matches the first character of the word, start DFS
                if board[i][j] == word[0] and solve(i, j, 0):
                    return True

        # Word not found
        return False

# Time Complexity (TC):
# - In the worst case, we might visit every cell multiple times, leading to an O(M * N * 4^L) complexity.
#   - M and N are the dimensions of the board.
#   - L is the length of the word.
#   - Each cell may branch in 4 directions, creating a branching factor of 4^L.

# Space Complexity (SC):
# - The space complexity is O(L) for the recursive call stack and O(L) for the visited set.
#   - Here, L is the length of the word, which is the maximum depth of the recursion.
#   - Thus, SC is O(L) overall due to the depth-first search with backtracking.
