class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
        Calculate the maximum matrix sum by adjusting signs if necessary.
        
        :param matrix: List of lists of integers representing the matrix
        :return: Maximum possible sum of matrix elements after flipping signs
        """
        neg_count = 0  # Count of negative numbers
        total_sum = 0  # Total sum of absolute values of matrix elements
        min_abs_value = float('inf')  # Minimum absolute value in the matrix
        
        for row in matrix:
            for value in row:
                total_sum += abs(value)  # Add absolute value to the sum
                if value < 0:
                    neg_count += 1  # Count negative values
                # Update minimum absolute value
                min_abs_value = min(min_abs_value, abs(value))
        
        # If there is an even count of negative numbers, we can flip all signs
        if neg_count % 2 == 0:
            return total_sum
        else:
            # If there is an odd count of negative numbers, we must subtract twice
            # the smallest absolute value to maximize the sum.
            return total_sum - 2 * min_abs_value

# Time Complexity (TC): O(n^2)
# - We iterate through all elements of the matrix once, where n is the number of rows or columns.
# - For an n x n matrix, the time complexity is O(n^2).

# Space Complexity (SC): O(1)
# - No additional data structures are used. Only a few variables are maintained, so the space complexity is constant.
