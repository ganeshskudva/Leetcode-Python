class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """
        Function to find the maximum number of equal rows after performing row flips.

        Parameters:
            matrix (List[List[int]]): 2D binary matrix.

        Returns:
            int: Maximum number of equal rows after flips.
        """
        row_patterns = defaultdict(int)

        for row in matrix:
            # Generate a key to represent the pattern of the row and its flipped version
            original_pattern = tuple(row)
            flipped_pattern = tuple(1 - cell for cell in row)

            # Count both the original and flipped patterns
            row_patterns[original_pattern] += 1
            row_patterns[flipped_pattern] += 1

        # Maximum count of any pattern (either original or flipped)
        return max(row_patterns.values())

# Time Complexity:
#     O(r * c):
#         - Each row is processed once, and comparing or generating flipped rows is O(c).
#         - The hashing mechanism ensures efficient lookup and grouping.

# Space Complexity:
#     O(r * c):
#         - Space is used for storing patterns in the hash map.