class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Convert a string to a 32-bit signed integer.

        Args:
        s (str): Input string.

        Returns:
        int: The integer representation of the string, clamped within the 32-bit signed integer range.

        Time Complexity: O(n), where n is the length of the string.
            - We iterate through the string once.
        Space Complexity: O(1), as no extra space is used.
        """
        if not s:  # If the string is empty, return 0
            return 0

        i, sign, base = 0, 1, 0  # Initialize index, sign, and base value
        max_int, min_int = 2**31 - 1, -2**31  # Define 32-bit signed integer limits

        # Skip leading whitespaces
        while i < len(s) and s[i] == ' ':
            i += 1

        # Check for a sign character ('+' or '-')
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1  # Update the sign based on the character
            i += 1

        # Process numerical digits and convert to integer
        while i < len(s) and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')  # Convert character to integer value
            
            # Check for overflow/underflow
            if base > (max_int // 10) or (base == max_int // 10 and digit > 7):
                return max_int if sign == 1 else min_int
            
            base = 10 * base + digit  # Update the base value
            i += 1

        return base * sign  # Return the final result with the appropriate sign

# Time Complexity: O(n), where n is the length of the input string.
# Space Complexity: O(1), as the function uses constant space.

