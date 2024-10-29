from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # Initialize count of cells with odd values
        cnt = 0
        # Row array to track increments in each row (length m)
        row = [0] * m
        # Column array to track increments in each column (length n)
        col = [0] * n

        # Update row and column counts based on indices
        # For each index in indices, increment the respective row and column counts
        for r, c in indices:
            row[r] += 1
            col[c] += 1

        # Calculate cells with odd values
        # Iterate over each cell and determine if the sum of row and column increments is odd
        for i in range(m):
            for j in range(n):
                cnt += (row[i] + col[j]) % 2  # Add 1 to cnt if sum is odd

        return cnt

# Time Complexity (TC):
# The code has two main loops:
# 1. The first loop iterates through `indices`, which has length `k`. So, it takes O(k).
# 2. The second nested loop iterates over each cell in the grid, i.e., O(m * n).
# Thus, the overall time complexity is O(k + m * n).

# Space Complexity (SC):
# The space complexity is O(m + n) for the row and column arrays.
# These arrays store the increment counts for each row and column.
