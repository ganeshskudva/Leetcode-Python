# Using set
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # To store indices of unmatched '('
        to_remove = set()  # To store indices of characters to remove
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)  # Record index of '('
            elif ch == ')':
                if stack:
                    stack.pop()  # Match with a previous '('
                else:
                    to_remove.add(i)  # Unmatched ')', mark for removal
        
        # Add unmatched '(' indices to to_remove
        to_remove.update(stack)
        
        # Build the result string by skipping indices in to_remove
        result = ''.join(ch for i, ch in enumerate(s) if i not in to_remove)
        
        return result

# Time Complexity (TC): O(n), where n is the length of the string.
# - We iterate over the string once to identify unmatched parentheses (O(n)).
# - We iterate again to construct the result string (O(n)).
# Total: O(n).

# Space Complexity (SC): O(n)
# - `stack` can store up to O(n) indices for unmatched '('.
# - `to_remove` can store up to O(n) indices for unmatched parentheses.
# - The resulting string construction uses additional space proportional to the input size.
# Total: O(n).


# Convert input string to list & modify
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Convert the string to a list to allow in-place modifications
        s = list(s)
        stack = []  # Stack to store indices of unmatched '(' characters

        # First pass: Process each character to remove invalid ')'
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Store index of '(' to match later
            elif char == ')':
                if stack:
                    stack.pop()  # Match with a previous '('
                else:
                    s[i] = ''  # Remove unmatched ')'

        # Second pass: Remove any unmatched '(' remaining in the stack
        while stack:
            s[stack.pop()] = ''  # Remove unmatched '(' by setting it to an empty string

        # Join the list back into a string, skipping all removed characters
        return ''.join(s)

# Time Complexity (TC): O(n), where n is the length of the string.
# - The first loop goes through each character once to process and identify unmatched parentheses.
# - The second loop removes unmatched '(' characters using the stack indices.

# Space Complexity (SC): O(n).
# - The `stack` stores indices of unmatched '(' characters, which could be at most n/2 in the worst case.
# - Additionally, `s` is converted to a list, which uses O(n) space.

