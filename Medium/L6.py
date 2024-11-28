class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Base case: If there's only one row or fewer, return the string as is.
        if numRows <= 1:
            return s
        
        # Initialize a list of lists to hold characters for each row.
        rows = [[] for _ in range(numRows)]
        
        # Variables to track the current row (idx) and direction (dir).
        idx, dir = 0, -1

        # Iterate through each character in the input string.
        for char in s:
            # Append the character to the corresponding row.
            rows[idx].append(char)
            
            # Change direction at the first or last row.
            if idx == 0 or idx == numRows - 1:
                dir = -dir
            
            # Move to the next row based on the direction.
            idx += dir

        # Join characters for each row and then join all rows to form the final string.
        return "".join("".join(row) for row in rows)

# Time Complexity (TC): O(n), where n is the length of the input string `s`.
# Each character is processed exactly once.

# Space Complexity (SC): O(n), where n is the length of the input string `s`.
# This is due to the space required to store characters in the `rows` list.
