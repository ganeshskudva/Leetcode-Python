class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # st_size keeps track of unmatched opening '(' brackets
        # mismatch keeps track of unmatched closing ')' brackets
        st_size = mismatch = 0
        
        # Iterate through each character in the string
        for c in s:
            if c == '(':  # For each opening bracket, increase the st_size (stack size)
                st_size += 1
            elif c == ')' and st_size:  # If a closing bracket and there's an unmatched '('
                st_size -= 1  # Match this closing bracket with an open one (reduce st_size)
            else:
                mismatch += 1  # If no matching '(' is available, increase mismatch count
        
        # Return the total number of unmatched brackets (unmatched '(' + unmatched ')')
        return st_size + mismatch

# Time Complexity (TC): 
# The algorithm iterates over the input string once, performing constant-time operations
# for each character. Therefore, the time complexity is O(n), where n is the length of the string `s`.

# Space Complexity (SC):
# The algorithm uses a constant amount of extra space for the variables `st_size` and `mismatch`, 
# irrespective of the input size. Thus, the space complexity is O(1).
