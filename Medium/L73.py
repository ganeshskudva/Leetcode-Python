class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modify the matrix in-place such that if an element is 0, 
        its entire row and column are set to 0.
        """
        # Get dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        
        # Flags to track if the first row and first column should be set to zero
        fr, fc = False, False
        
        # First pass: Identify which rows and columns need to be zeroed
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # If any element in the first row is zero, mark fr to True
                    if i == 0:
                        fr = True
                    # If any element in the first column is zero, mark fc to True
                    if j == 0:
                        fc = True
                    # Use the first row and first column to mark the zero rows and columns
                    matrix[0][j] = 0  # Mark the top of the column
                    matrix[i][0] = 0  # Mark the left of the row

        # Second pass: Use markers in the first row and column to set elements to zero
        for i in range(1, m):
            for j in range(1, n):
                # If the first element in the row or column is zero, set the element to zero
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # If fr is True, set the entire first row to zero
        if fr:
            for j in range(n):
                matrix[0][j] = 0
        
        # If fc is True, set the entire first column to zero
        if fc:
            for i in range(m):
                matrix[i][0] = 0
