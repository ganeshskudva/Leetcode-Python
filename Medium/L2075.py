class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # Calculate the number of columns in the matrix
        cols, res = len(encodedText) // rows, []  
        
        # Traverse diagonally across the encoded text
        # Outer loop runs 'cols' times
        for i in range(cols):  
            # Inner loop traverses diagonally, increments by cols + 1
            for j in range(i, len(encodedText), cols + 1):  
                res.append(encodedText[j])  # Append characters to result list

        # Join the result list into a string and remove trailing spaces
        return ''.join(res).rstrip()

# Time Complexity (TC): O(n)
#   - Outer loop runs 'cols' times, where cols = len(encodedText) // rows.
#   - Inner loop runs len(encodedText) / cols times, making the total iterations proportional to len(encodedText).
#   - Overall, the traversal is linear with respect to the size of the input, O(n), where n = len(encodedText).

# Space Complexity (SC): O(n)
#   - The space required for the 'res' list is proportional to the size of the decoded text, which can be up to len(encodedText).
#   - The join operation also temporarily uses additional space but is linear in complexity.
