class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Check if the matrix is empty; return False if it is
        if not matrix:
            return False
        
        # Get the dimensions of the matrix (m = number of rows, n = number of columns)
        m, n = len(matrix), len(matrix[0])
        
        # Set up the initial binary search boundaries in the 1D flattened array view of the matrix
        lo, hi = 0, m * n - 1
        
        # Perform binary search
        while lo <= hi:
            # Calculate the middle index in the "1D view" of the matrix
            mid = lo + (hi - lo) // 2
            
            # Convert the 1D index (mid) back to a 2D index (r, c) using matrix dimensions
            r, c = mid // n, mid % n
            
            # Check if the element at the 2D index (r, c) matches the target
            if matrix[r][c] == target:
                return True  # If we found the target, return True
            
            # If the current element is less than the target, discard the left half
            if matrix[r][c] < target:
                lo = mid + 1  # Move the low pointer to the right half
            
            # If the current element is greater than the target, discard the right half
            else:
                hi = mid - 1  # Move the high pointer to the left half
        
        # If the loop finishes without finding the target, return False
        return False
