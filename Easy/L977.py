class Solution:
    def sortedSquares(self, A):
        n = len(A)
        result = [0] * n  # Create an empty array of size n to store the result
        i, j = 0, n - 1  # Initialize two pointers: i at the beginning, j at the end

        # Iterate from the end of the result array to the start
        for p in range(n - 1, -1, -1):
            # Compare absolute values of the numbers at pointers i and j
            if abs(A[i]) > abs(A[j]):
                # Square the value at i and store it in the result, then move pointer i forward
                result[p] = A[i] * A[i]
                i += 1
            else:
                # Square the value at j and store it in the result, then move pointer j backward
                result[p] = A[j] * A[j]
                j -= 1

        return result