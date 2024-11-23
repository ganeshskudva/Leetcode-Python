class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Finds the largest square containing only '1's and returns its area.

        :param matrix: A 2D binary matrix (as a list of lists of strings).
        :return: The area of the largest square of '1's.
        """
        mp = {}  # Memoization dictionary to store results of subproblems
        m, n = len(matrix), len(matrix[0])  # Dimensions of the matrix

        def isValid(x, y):
            """
            Checks if the position (x, y) is within bounds and has a value of '1'.

            :param x: Row index.
            :param y: Column index.
            :return: True if the position is valid and contains '1', otherwise False.
            """
            return 0 <= x < m and 0 <= y < n and matrix[x][y] == '1'

        def solve(x, y):
            """
            Computes the size of the largest square with top-left corner at (x, y).
            Uses memoization to avoid redundant computations.

            :param x: Row index.
            :param y: Column index.
            :return: The side length of the largest square with top-left corner at (x, y).
            """
            if not isValid(x, y):  # If the cell is invalid or not '1', return 0.
                return 0

            key = (x, y)  # Create a unique key for the current cell
            if key in mp:  # If the result is already computed, return it.
                return mp[key]

            # Compute the largest square using the results of subproblems
            mp[key] = 1 + min(
                solve(x + 1, y),       # Down
                solve(x, y + 1),       # Right
                solve(x + 1, y + 1)    # Diagonal
            )
            return mp[key]

        ans = 0  # Variable to store the maximum side length of a square
        for i in range(m):  # Iterate over all rows
            for j in range(n):  # Iterate over all columns
                if matrix[i][j] == '1':  # Only consider cells with '1'
                    ans = max(ans, solve(i, j))  # Update the maximum side length

        return ans**2  # Return the area of the largest square

# Time Complexity (TC):
# O(m * n) - Each cell in the matrix is visited at most once due to memoization.
#            The recursive calls for a cell depend on its adjacent cells, but
#            memoization ensures no cell is recomputed.

# Space Complexity (SC):
# O(m * n) - Memoization dictionary stores results for all cells.
# O(min(m, n)) - Recursive call stack depth, which is limited by the matrix diagonal.
# Total: O(m * n) for large matrices where memoization dominates.
