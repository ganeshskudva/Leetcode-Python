class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Initialize the result list that will store elements in spiral order
        res = []
        
        # Continue the process until the matrix is empty
        while matrix:
            # Remove the first row from the matrix and append it to the result list
            res.extend(matrix.pop(0))
            
            # Transpose the remaining matrix (rotate it 90 degrees counterclockwise)
            # This is achieved by:
            # 1. Using zip(*matrix) to transpose the matrix.
            # 2. Convert the transposed result into a list of lists using [*zip(*matrix)].
            # 3. Reverse the rows to simulate a 90-degree counterclockwise rotation.
            matrix = [*zip(*matrix)][::-1]
        
        # Return the result list, which now contains the elements in spiral order
        return res
