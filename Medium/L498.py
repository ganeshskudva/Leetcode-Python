from typing import List, Dict

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # Edge case: If the matrix is empty, return an empty list
        if not matrix or not matrix[0]:
            return []

        # Dictionary to store each diagonal's elements.
        # Keys are the diagonal levels (i + j), values are lists of elements on that diagonal
        diagonals: Dict[int, List[int]] = {}
        
        # Traverse the matrix to populate the diagonals dictionary
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # Calculate the diagonal level as the sum of row index and column index (i + j)
                diagonal_level = i + j
                
                # If this diagonal level is not in the dictionary, initialize it with an empty list
                if diagonal_level not in diagonals:
                    diagonals[diagonal_level] = []
                
                # Append the current element to the corresponding diagonal level in the dictionary
                diagonals[diagonal_level].append(matrix[i][j])

        # Prepare the final result list to store elements in the required diagonal order
        result = []

        # Process each diagonal level in order
        for level in sorted(diagonals.keys()):
            # If the diagonal level is even, reverse the order of elements before adding to the result
            # This creates the "snake" effect for every other diagonal
            if level % 2 == 0:
                result.extend(reversed(diagonals[level]))
            else:
                result.extend(diagonals[level])

        return result

# Time Complexity (TC):
# - We traverse each element in the matrix once to populate the `diagonals` dictionary, which takes O(m * n),
#   where m is the number of rows and n is the number of columns.
# - Sorting the dictionary keys and constructing the result list takes O(d), where d is the number of diagonals (m + n - 1).
# - Overall time complexity: O(m * n) since the traversal dominates the sorting of a small number of diagonals.

# Space Complexity (SC):
# - The `diagonals` dictionary holds up to m + n - 1 diagonals, each storing a subset of the elements in the matrix.
#   In the worst case, this requires O(m * n) space to store all elements.
# - The final `result` list requires O(m * n) space as well.
# - Overall space complexity: O(m * n).
