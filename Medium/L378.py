from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Helper function to count the number of elements less than or equal to x
        # Time Complexity for each call: O(N), where N is the number of rows in the matrix
        def count_less_or_equal(x):
            cnt = 0  # Counter for elements less than or equal to x
            col = len(matrix[0]) - 1  # Start from the last column of each row
            
            # For each row, count how many elements are <= x
            for row in range(len(matrix)):
                while col >= 0 and matrix[row][col] > x:
                    col -= 1  # Move left if element is greater than x
                cnt += (col + 1)  # Add (col + 1) to count, as all elements in this row up to col are <= x
            return cnt
        
        # Initialize binary search boundaries based on the smallest and largest elements in the matrix
        lo, hi = matrix[0][0], matrix[-1][-1]
        res = -1
        
        # Binary search to find the kth smallest element
        while lo <= hi:
            mid = lo + (hi - lo) // 2  # Calculate the middle element
            # If count of elements <= mid is at least k, mid could be the kth smallest
            if count_less_or_equal(mid) >= k:
                res = mid  # Store mid as a candidate for kth smallest
                hi = mid - 1  # Try for a smaller value to find the smallest candidate
            else:
                lo = mid + 1  # Increase lo to find a larger value
            
        return res

# Time Complexity (TC):
# - Binary search on the range [lo, hi] takes O(log(max - min)), where max and min are the largest and smallest values in the matrix.
# - For each iteration in binary search, we call `count_less_or_equal`, which takes O(N) where N is the number of rows (and columns) in the matrix.
# - Overall time complexity: O(N * log(max - min)).

# Space Complexity (SC):
# - The only extra space used is a few variables for binary search and the count.
# - Therefore, the space complexity is O(1).
