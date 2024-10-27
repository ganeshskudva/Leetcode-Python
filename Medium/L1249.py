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

