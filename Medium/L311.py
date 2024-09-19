from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # m: number of rows in mat1
        # n: number of columns in mat1 (which is also the number of rows in mat2)
        # num_times: number of columns in mat2
        m, n, num_times = len(mat1), len(mat2), len(mat2[0])
        
        # Initialize the result matrix 'res' with dimensions m x num_times, filled with zeros
        res = [[0] * num_times for _ in range(m)]

        # Loop over each row of mat1
        for i in range(m):
            # Loop over each column of mat1 (or equivalently each row of mat2)
            for k in range(n):
                # If the current element in mat1 is non-zero, we proceed with the multiplication
                if mat1[i][k] != 0:
                    # Loop over each column of mat2
                    for j in range(num_times):
                        # Only multiply and accumulate if the current element in mat2 is also non-zero
                        if mat2[k][j] != 0:
                            # Update the result matrix at position (i, j) with the product of
                            # mat1[i][k] and mat2[k][j] and accumulate it to the current value
                            res[i][j] += mat1[i][k] * mat2[k][j]

        # Return the final result matrix after completing the multiplication
        return res
