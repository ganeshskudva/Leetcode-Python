from collections import defaultdict
from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = defaultdict(int)  # Memoization dictionary to store results of subproblems
        m, n, cnt = len(matrix), len(matrix[0]), 0  # Matrix dimensions and counter for square submatrices
        dirs = [[0, -1], [-1, 0], [-1, -1]]  # Directions to check the left, top, and top-left cells

        def is_valid(x, y):
            # Check if the cell (x, y) is within bounds and has a value of 1
            return 0 <= x < m and 0 <= y < n and matrix[x][y] == 1

        def solve(i, j):
            # Recursively calculate the size of the largest square submatrix ending at (i, j)
            if not is_valid(i, j):
                return 0  # Return 0 if the cell is out of bounds or has a value of 0
            
            key = (i, j)  # Use (i, j) as a key for memoization
            if key in dp:
                return dp[key]  # Return cached result if already computed
            
            # Initialize to infinity for finding the minimum size of squares possible from neighbors
            mn = float('inf')
            for dx, dy in dirs:
                mn = min(mn, solve(i + dx, j + dy))  # Recursively get minimum from neighboring squares
            
            dp[key] = 1 + mn  # Store the result in dp; include current cell to form a larger square
            return dp[key]  # Return the size of the square ending at (i, j)
        
        for r in range(m):
            for c in range(n):
                cnt += solve(r, c)  # Count squares ending at each cell in the matrix
        
        return cnt  # Total count of square submatrices

# Time Complexity (TC): O(m * n), where m is the number of rows and n is the number of columns.
# Each cell is visited once, and memoization ensures each subproblem is solved only once.

# Space Complexity (SC): O(m * n) for the dp dictionary to store the result of each cell. 
# The recursion stack can also use up to O(m * n) in the worst case if we recurse through all cells without memoization.
