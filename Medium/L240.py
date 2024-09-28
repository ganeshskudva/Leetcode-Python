class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Check if the matrix is empty; if it is, return False as there's nothing to search
        if not matrix:
            return False

        # Start the search from the top-right corner of the matrix
        row, col = 0, len(matrix[0]) - 1  # row = first row, col = last column

        # Continue the search as long as row is within matrix bounds and col is non-negative
        while row <= len(matrix) - 1 and col >= 0:
            # If the target matches the current element, return True
            if target == matrix[row][col]:
                return True
            # If the target is smaller than the current element, move left (decrease column)
            elif target < matrix[row][col]:
                col -= 1
            # If the target is larger than the current element, move down (increase row)
            else:
                row += 1

        # If the target is not found after searching the matrix, return False
        return False
