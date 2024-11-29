class Solution:
    def checkValidString(self, s: str) -> bool:
        # Initialize counters for the minimum and maximum possible open parentheses
        min_open, max_open = 0, 0

        # Iterate through each character in the string
        for char in s:
            if char == '(':
                # If it's an opening parenthesis:
                # - Increment both min_open and max_open since '(' always adds to unmatched '('
                min_open += 1
                max_open += 1
            elif char == ')':
                # If it's a closing parenthesis:
                # - Decrement both min_open and max_open since ')' reduces unmatched '('
                min_open -= 1
                max_open -= 1
            elif char == '*':
                # If it's a '*':
                # - It can act as '(' (increment max_open)
                # - Or as ')' (decrement min_open)
                # - Or as an empty string (do nothing to min_open or max_open)
                min_open -= 1
                max_open += 1

            # If max_open becomes negative, too many ')' have been encountered,
            # making the string invalid
            if max_open < 0:
                return False

            # Clamp min_open to 0 because we cannot have fewer than 0 unmatched '('
            min_open = max(min_open, 0)

        # At the end of the loop:
        # - If min_open == 0, all unmatched '(' can be balanced
        # - Otherwise, the string is invalid
        return min_open == 0

# Time Complexity (TC): O(n)
# Explanation:
# - The algorithm iterates through the string once, processing each character in O(1) time.
# - Each operation (comparison, increment, or clamping) is constant time.
# - Total complexity: O(n), where n is the length of the string.

# Space Complexity (SC): O(1)
# Explanation:
# - The algorithm uses two integer variables, min_open and max_open, which require constant space.
# - No additional data structures are used.
# - Total space complexity: O(1).
