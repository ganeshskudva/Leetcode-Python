from collections import defaultdict
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Dictionary to store the frequency of rows as tuples
        m = defaultdict(int)
        cnt = 0

        # Count the frequency of each row (converted to a tuple)
        for row in grid:
            m[tuple(row)] += 1

        # Check for matching columns
        for i in range(len(grid[0])):  # Iterate through columns
            col = []
            for j in range(len(grid)):  # Build the column as a list
                col.append(grid[j][i])
            # Add the frequency of this column (if it matches any row) to the count
            cnt += m[tuple(col)]

        return cnt

# Time Complexity (TC):
# O(n^2), where n is the number of rows/columns in the grid:
#   - Constructing the dictionary of rows takes O(n^2) as each row has n elements.
#   - Iterating through columns and matching them with rows also takes O(n^2).

# Space Complexity (SC):
# O(n^2):
#   - The `defaultdict` stores up to n rows as tuples, each of size n, requiring O(n^2) space.
#   - Temporary space for storing columns (`col`) is O(n) but negligible compared to O(n^2).
